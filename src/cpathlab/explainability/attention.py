from __future__ import annotations

import torch


def attention_to_grid(weights: torch.Tensor, grid_shape: tuple[int, int]) -> torch.Tensor:
    if weights.ndim == 2:
        weights = weights[0]
    if weights.numel() != grid_shape[0] * grid_shape[1]:
        raise ValueError("attention size does not match grid")
    grid = weights.reshape(grid_shape)
    grid -= grid.min()
    return grid / grid.max().clamp_min(1e-8)
