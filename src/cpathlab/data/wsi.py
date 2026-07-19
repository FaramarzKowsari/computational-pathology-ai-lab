from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path

import numpy as np
from PIL import Image


def tissue_mask(image: Image.Image, saturation_threshold: int = 20, brightness_threshold: int = 235) -> np.ndarray:
    rgb = np.asarray(image.convert("RGB"), dtype=np.uint8)
    max_channel = rgb.max(axis=2).astype(np.int16)
    min_channel = rgb.min(axis=2).astype(np.int16)
    saturation = max_channel - min_channel
    brightness = rgb.mean(axis=2)
    return (saturation >= saturation_threshold) & (brightness <= brightness_threshold)


def iter_patches(
    image: Image.Image,
    patch_size: int = 256,
    stride: int | None = None,
    min_tissue_fraction: float = 0.5,
) -> Iterator[tuple[tuple[int, int], Image.Image]]:
    stride = stride or patch_size
    mask = tissue_mask(image)
    width, height = image.size
    for y in range(0, max(1, height - patch_size + 1), stride):
        for x in range(0, max(1, width - patch_size + 1), stride):
            local = mask[y:y + patch_size, x:x + patch_size]
            if local.shape == (patch_size, patch_size) and float(local.mean()) >= min_tissue_fraction:
                yield (x, y), image.crop((x, y, x + patch_size, y + patch_size))


def open_slide_thumbnail(path: str | Path, max_size: int = 2048) -> Image.Image:
    """Open a conventional image or an OpenSlide-compatible WSI thumbnail."""
    path = Path(path)
    try:
        import openslide  # type: ignore
        slide = openslide.OpenSlide(str(path))
        return slide.get_thumbnail((max_size, max_size)).convert("RGB")
    except (ImportError, OSError):
        with Image.open(path) as image:
            result = image.convert("RGB")
            result.thumbnail((max_size, max_size))
            return result.copy()
