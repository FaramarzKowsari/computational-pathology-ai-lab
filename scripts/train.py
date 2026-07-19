from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd
import torch
from torch import nn
from torch.utils.data import DataLoader

from cpathlab.config import ExperimentConfig
from cpathlab.data.datasets import PatchDataset
from cpathlab.evaluation.metrics import classification_metrics
from cpathlab.models import create_model
from cpathlab.training.engine import predict_loader, resolve_device, train_one_epoch
from cpathlab.training.reproducibility import seed_everything


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = ExperimentConfig.from_yaml(args.config)
    seed_everything(config.data.seed)
    frame = pd.read_csv("data/processed/manifest.csv")
    train_ds = PatchDataset(frame[frame.split == "train"], config.data.image_dir)
    val_ds = PatchDataset(frame[frame.split == "val"], config.data.image_dir)
    train_loader = DataLoader(train_ds, batch_size=config.training.batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=config.training.batch_size)
    device = resolve_device(config.training.device)
    model = create_model(config.model.name, config.model.num_classes, config.model.pretrained).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=config.training.learning_rate, weight_decay=config.training.weight_decay)
    criterion = nn.CrossEntropyLoss()
    for epoch in range(config.training.epochs):
        loss = train_one_epoch(model, train_loader, optimizer, criterion, device)
        print(f"epoch={epoch+1} loss={loss:.5f}")
    y_true, probabilities = predict_loader(model, val_loader, device)
    metrics = classification_metrics(y_true, probabilities)
    Path("models").mkdir(exist_ok=True)
    Path("reports").mkdir(exist_ok=True)
    torch.save(model.state_dict(), "models/baseline.pt")
    Path("reports/metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
