from __future__ import annotations

import torch
from torch import nn


class FocalLoss(nn.Module):
    def __init__(self, gamma: float = 2.0, alpha: float | None = None) -> None:
        super().__init__()
        self.gamma = gamma
        self.alpha = alpha

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        ce = torch.nn.functional.cross_entropy(logits, targets, reduction="none")
        probability = torch.exp(-ce)
        loss = (1 - probability).pow(self.gamma) * ce
        if self.alpha is not None:
            weights = torch.where(targets == 1, self.alpha, 1 - self.alpha)
            loss = loss * weights
        return loss.mean()
