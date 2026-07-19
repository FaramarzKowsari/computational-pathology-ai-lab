from __future__ import annotations

import numpy as np
import torch
from PIL import Image, ImageEnhance


def reinhard_normalize(image: Image.Image, target_mean: tuple[float, float, float] = (180, 145, 175), target_std: tuple[float, float, float] = (35, 40, 35)) -> Image.Image:
    """Simple RGB moment matching; useful as a transparent educational baseline."""
    array = np.asarray(image.convert("RGB"), dtype=np.float32)
    mean = array.reshape(-1, 3).mean(axis=0)
    std = array.reshape(-1, 3).std(axis=0).clip(1.0)
    normalized = (array - mean) / std
    normalized = normalized * np.asarray(target_std) + np.asarray(target_mean)
    return Image.fromarray(normalized.clip(0, 255).astype(np.uint8))


def augment_image(image: Image.Image, rng: np.random.Generator | None = None) -> Image.Image:
    rng = rng or np.random.default_rng()
    result = image.convert("RGB")
    if rng.random() < 0.5:
        result = result.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    if rng.random() < 0.5:
        result = result.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    result = result.rotate(int(rng.choice([0, 90, 180, 270])))
    result = ImageEnhance.Color(result).enhance(float(rng.uniform(0.85, 1.15)))
    result = ImageEnhance.Brightness(result).enhance(float(rng.uniform(0.9, 1.1)))
    return result


def image_to_tensor(image: Image.Image, size: int = 96) -> torch.Tensor:
    resized = image.convert("RGB").resize((size, size), Image.Resampling.BILINEAR)
    array = np.asarray(resized, dtype=np.float32) / 255.0
    tensor = torch.from_numpy(array).permute(2, 0, 1)
    mean = torch.tensor([0.5, 0.5, 0.5]).view(3, 1, 1)
    std = torch.tensor([0.25, 0.25, 0.25]).view(3, 1, 1)
    return (tensor - mean) / std
