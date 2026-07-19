from __future__ import annotations

import torch
from torch import nn


class GradCAM:
    def __init__(self, model: nn.Module, target_layer: nn.Module) -> None:
        self.model = model
        self.activations: torch.Tensor | None = None
        self.gradients: torch.Tensor | None = None
        target_layer.register_forward_hook(self._forward_hook)
        target_layer.register_full_backward_hook(self._backward_hook)

    def _forward_hook(self, _module: nn.Module, _inputs: tuple[torch.Tensor, ...], output: torch.Tensor) -> None:
        self.activations = output

    def _backward_hook(self, _module: nn.Module, _grad_input: tuple[torch.Tensor, ...], grad_output: tuple[torch.Tensor, ...]) -> None:
        self.gradients = grad_output[0]

    def __call__(self, image: torch.Tensor, class_index: int | None = None) -> torch.Tensor:
        self.model.zero_grad(set_to_none=True)
        logits = self.model(image)
        index = int(logits.argmax(dim=1)[0]) if class_index is None else class_index
        logits[:, index].sum().backward()
        if self.activations is None or self.gradients is None:
            raise RuntimeError("Hooks did not capture tensors")
        weights = self.gradients.mean(dim=(2, 3), keepdim=True)
        cam = torch.relu((weights * self.activations).sum(dim=1, keepdim=True))
        cam = torch.nn.functional.interpolate(cam, size=image.shape[-2:], mode="bilinear", align_corners=False)
        cam -= cam.amin(dim=(2, 3), keepdim=True)
        cam /= cam.amax(dim=(2, 3), keepdim=True).clamp_min(1e-8)
        return cam.detach()
