from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import torch
from torch import nn


class FeatureEncoder(Protocol):
    output_dim: int
    def encode(self, images: torch.Tensor) -> torch.Tensor: ...


@dataclass(slots=True)
class FoundationModelMetadata:
    name: str
    source: str
    license: str
    output_dim: int
    weights_included: bool = False


class FoundationModelAdapter(nn.Module):
    """Adapter for externally obtained pathology encoders.

    The repository does not redistribute gated or restricted weights. Supply a trusted
    encoder that returns one feature vector per image.
    """
    def __init__(self, encoder: nn.Module, output_dim: int, num_classes: int = 2, freeze: bool = True) -> None:
        super().__init__()
        self.encoder = encoder
        self.output_dim = output_dim
        if freeze:
            for parameter in self.encoder.parameters():
                parameter.requires_grad = False
        self.head = nn.Linear(output_dim, num_classes)

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        features = self.encoder(images)
        if isinstance(features, dict):
            features = features.get("features", next(iter(features.values())))
        if features.ndim > 2:
            features = features.flatten(1)
        return self.head(features)
