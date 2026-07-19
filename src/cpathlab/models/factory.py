from __future__ import annotations

from typing import Any, cast

from torch import nn

from .baseline import BaselineCNN
from .vit import TinyVisionTransformer


def _replace_classifier(model: nn.Module, name: str, num_classes: int) -> nn.Module:
    dynamic: Any = model
    if name.startswith("resnet"):
        dynamic.fc = nn.Linear(dynamic.fc.in_features, num_classes)
    elif name.startswith("densenet"):
        dynamic.classifier = nn.Linear(dynamic.classifier.in_features, num_classes)
    elif name.startswith("efficientnet") or name.startswith("convnext"):
        last = dynamic.classifier[-1]
        dynamic.classifier[-1] = nn.Linear(last.in_features, num_classes)
    return cast(nn.Module, dynamic)


def create_model(name: str, num_classes: int = 2, pretrained: bool = False) -> nn.Module:
    normalized = name.lower().replace("-", "_")
    if normalized in {"baseline", "baseline_cnn"}:
        return BaselineCNN(num_classes=num_classes)
    if normalized in {"tiny_vit", "vit"}:
        return TinyVisionTransformer(num_classes=num_classes)
    try:
        from torchvision import models
    except ImportError as exc:
        raise RuntimeError("torchvision is required for transfer-learning models") from exc
    constructors = {
        "resnet18": models.resnet18,
        "resnet50": models.resnet50,
        "densenet121": models.densenet121,
        "efficientnet_b0": models.efficientnet_b0,
        "convnext_tiny": models.convnext_tiny,
    }
    if normalized not in constructors:
        raise ValueError(f"Unknown model: {name}")
    weights = "DEFAULT" if pretrained else None
    model = constructors[normalized](weights=weights)
    return _replace_classifier(model, normalized, num_classes)
