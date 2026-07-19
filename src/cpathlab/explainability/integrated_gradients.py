from __future__ import annotations

import torch
from torch import nn


def integrated_gradients(model: nn.Module, image: torch.Tensor, target: int, steps: int = 32, baseline: torch.Tensor | None = None) -> torch.Tensor:
    baseline = torch.zeros_like(image) if baseline is None else baseline
    gradients: list[torch.Tensor] = []
    for alpha in torch.linspace(0, 1, steps, device=image.device):
        scaled = (baseline + alpha * (image - baseline)).detach().requires_grad_(True)
        score = model(scaled)[:, target].sum()
        gradient = torch.autograd.grad(score, scaled)[0]
        gradients.append(gradient)
    average = torch.stack(gradients).mean(dim=0)
    return (image - baseline) * average
