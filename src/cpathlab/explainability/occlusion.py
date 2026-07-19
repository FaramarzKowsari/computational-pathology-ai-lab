from __future__ import annotations

import torch
from torch import nn


@torch.inference_mode()
def occlusion_sensitivity(model: nn.Module, image: torch.Tensor, target: int, window: int = 16, stride: int = 8, fill: float = 0.0) -> torch.Tensor:
    baseline = torch.softmax(model(image), dim=1)[:, target]
    heatmap = torch.zeros(image.shape[-2:], device=image.device)
    counts = torch.zeros_like(heatmap)
    for y in range(0, image.shape[-2] - window + 1, stride):
        for x in range(0, image.shape[-1] - window + 1, stride):
            occluded = image.clone()
            occluded[:, :, y:y+window, x:x+window] = fill
            drop = baseline - torch.softmax(model(occluded), dim=1)[:, target]
            heatmap[y:y+window, x:x+window] += drop.mean()
            counts[y:y+window, x:x+window] += 1
    return heatmap / counts.clamp_min(1)
