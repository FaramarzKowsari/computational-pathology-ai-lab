from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def _synthetic_patch(label: int, size: int, rng: np.random.Generator) -> Image.Image:
    base: np.ndarray = np.zeros((size, size, 3), dtype=np.uint8)
    base[..., 0] = rng.normal(220, 12, (size, size)).clip(0, 255)
    base[..., 1] = rng.normal(175, 16, (size, size)).clip(0, 255)
    base[..., 2] = rng.normal(205, 14, (size, size)).clip(0, 255)
    image = Image.fromarray(base, mode="RGB").filter(ImageFilter.GaussianBlur(0.7))
    draw = ImageDraw.Draw(image, "RGBA")
    cells = int(rng.integers(20, 45))
    for _ in range(cells):
        x, y = int(rng.integers(4, size - 4)), int(rng.integers(4, size - 4))
        r = int(rng.integers(2, 6))
        draw.ellipse((x - r, y - r, x + r, y + r), fill=(80, 30, 120, int(rng.integers(80, 170))))
    if label == 1:
        cx, cy = int(rng.integers(size // 3, 2 * size // 3)), int(rng.integers(size // 3, 2 * size // 3))
        for _ in range(int(rng.integers(12, 25))):
            x = int(np.clip(rng.normal(cx, size / 10), 3, size - 3))
            y = int(np.clip(rng.normal(cy, size / 10), 3, size - 3))
            r = int(rng.integers(3, 8))
            draw.ellipse((x-r, y-r, x+r, y+r), fill=(70, 10, 95, int(rng.integers(150, 230))))
    return image


def generate_synthetic_dataset(output: str | Path, samples: int = 40, size: int = 96, seed: int = 42) -> Path:
    """Generate non-clinical images for deterministic tests and demos."""
    root = Path(output)
    images = root / "images"
    images.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(seed)
    rows: list[dict[str, str | int]] = []
    for index in range(samples):
        label = index % 2
        name = f"synthetic_{index:04d}.png"
        _synthetic_patch(label, size, rng).save(images / name)
        rows.append({"image": name, "label": label, "group": f"synthetic_group_{index // 4:03d}"})
    manifest = root / "labels.csv"
    with manifest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["image", "label", "group"])
        writer.writeheader()
        writer.writerows(rows)
    return manifest
