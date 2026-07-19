from __future__ import annotations

import torch
from torch import nn


def _enable_dropout(module: nn.Module) -> None:
    if isinstance(module, nn.Dropout):
        module.train()


@torch.inference_mode()
def mc_dropout_predict(model: nn.Module, images: torch.Tensor, samples: int = 20) -> tuple[torch.Tensor, torch.Tensor]:
    model.eval()
    model.apply(_enable_dropout)
    probabilities = torch.stack([torch.softmax(model(images), dim=1) for _ in range(samples)])
    return probabilities.mean(dim=0), probabilities.std(dim=0)
