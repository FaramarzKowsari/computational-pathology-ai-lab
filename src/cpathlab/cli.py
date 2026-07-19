from __future__ import annotations

import json
from pathlib import Path
from typing import Annotated

import pandas as pd
import torch
import typer
from torch import nn
from torch.utils.data import DataLoader

from cpathlab.data.datasets import PatchDataset
from cpathlab.data.preprocessing import image_to_tensor
from cpathlab.data.splitting import split_manifest
from cpathlab.data.synthetic import generate_synthetic_dataset
from cpathlab.data.validation import validate_dataset
from cpathlab.evaluation.metrics import classification_metrics
from cpathlab.models import create_model
from cpathlab.training.engine import predict_loader, resolve_device, train_one_epoch
from cpathlab.training.reproducibility import seed_everything

app = typer.Typer(help="Computational Pathology AI Lab command line interface")


@app.command("generate-synthetic")
def generate_synthetic(output: Path = Path("data/example"), samples: int = 40, size: int = 96, seed: int = 42) -> None:
    manifest = generate_synthetic_dataset(output, samples=samples, size=size, seed=seed)
    typer.echo(f"Synthetic research-only dataset created: {manifest}")


@app.command("validate-data")
def validate_data(
    image_dir: Annotated[Path, typer.Option("--image-dir")],
    labels: Annotated[Path, typer.Option("--labels")],
) -> None:
    report = validate_dataset(image_dir, labels)
    typer.echo(json.dumps(report.to_dict(), indent=2))
    if not report.ok:
        raise typer.Exit(code=1)


@app.command("train-synthetic")
def train_synthetic(data_dir: Path = Path("data/example"), epochs: int = 1, output: Path = Path("models/demo.pt"), seed: int = 42) -> None:
    seed_everything(seed)
    torch.set_num_threads(min(2, torch.get_num_threads()))
    manifest_path = data_dir / "labels.csv"
    if not manifest_path.exists():
        generate_synthetic_dataset(data_dir, samples=40, seed=seed)
    frame = split_manifest(pd.read_csv(manifest_path), seed=seed)
    def transform(image: object) -> torch.Tensor:
        return image_to_tensor(image, size=32)  # type: ignore[arg-type]
    train = PatchDataset(frame[frame.split == "train"], data_dir / "images", transform=transform)
    val = PatchDataset(frame[frame.split == "val"], data_dir / "images", transform=transform)
    train_loader = DataLoader(train, batch_size=8, shuffle=True)
    val_loader = DataLoader(val, batch_size=8)
    device = resolve_device("auto")
    model = create_model("baseline_cnn").to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
    criterion = nn.CrossEntropyLoss()
    for epoch in range(epochs):
        loss = train_one_epoch(model, train_loader, optimizer, criterion, device)
        typer.echo(f"epoch={epoch + 1} loss={loss:.4f}")
    y_true, probabilities = predict_loader(model, val_loader, device)
    metrics = classification_metrics(y_true, probabilities)
    typer.echo("SYNTHETIC SMOKE METRICS - NOT A MEDICAL BENCHMARK")
    typer.echo(json.dumps(metrics, indent=2))
    output.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), output)


if __name__ == "__main__":
    app()
