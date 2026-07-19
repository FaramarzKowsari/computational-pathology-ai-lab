from __future__ import annotations

import torch
from torch import nn


class AttentionMIL(nn.Module):
    """Gated attention multiple-instance learning for slide-level bags."""
    def __init__(self, input_dim: int, hidden_dim: int = 128, num_classes: int = 2) -> None:
        super().__init__()
        self.value = nn.Sequential(nn.Linear(input_dim, hidden_dim), nn.Tanh())
        self.gate = nn.Sequential(nn.Linear(input_dim, hidden_dim), nn.Sigmoid())
        self.attention = nn.Linear(hidden_dim, 1)
        self.classifier = nn.Linear(input_dim, num_classes)

    def forward(self, instances: torch.Tensor, mask: torch.Tensor | None = None) -> tuple[torch.Tensor, torch.Tensor]:
        if instances.ndim != 3:
            raise ValueError("instances must have shape [batch, instances, features]")
        scores = self.attention(self.value(instances) * self.gate(instances)).squeeze(-1)
        if mask is not None:
            scores = scores.masked_fill(~mask.bool(), float("-inf"))
        weights = torch.softmax(scores, dim=1)
        pooled = torch.sum(instances * weights.unsqueeze(-1), dim=1)
        return self.classifier(pooled), weights
