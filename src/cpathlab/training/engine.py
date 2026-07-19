from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import torch
from torch import nn


def resolve_device(requested: str = "auto") -> torch.device:
    if requested == "auto":
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")
    return torch.device(requested)


def train_one_epoch(model: nn.Module, loader: Iterable[tuple[torch.Tensor, torch.Tensor]], optimizer: torch.optim.Optimizer, criterion: nn.Module, device: torch.device) -> float:
    model.train()
    losses: list[float] = []
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad(set_to_none=True)
        loss = criterion(model(images), labels)
        loss.backward()
        optimizer.step()
        losses.append(float(loss.detach().cpu()))
    return float(np.mean(losses)) if losses else float("nan")


@torch.inference_mode()
def predict_loader(model: nn.Module, loader: Iterable[tuple[torch.Tensor, torch.Tensor]], device: torch.device) -> tuple[np.ndarray, np.ndarray]:
    model.eval()
    probabilities: list[np.ndarray] = []
    targets: list[np.ndarray] = []
    for images, labels in loader:
        logits = model(images.to(device))
        probabilities.append(torch.softmax(logits, dim=1)[:, 1].cpu().numpy())
        targets.append(labels.numpy())
    return np.concatenate(targets), np.concatenate(probabilities)
