from __future__ import annotations

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter


def apply_shift(image: Image.Image, kind: str, severity: float = 0.5, seed: int = 42) -> Image.Image:
    severity = float(np.clip(severity, 0.0, 1.0))
    if kind == "brightness":
        return ImageEnhance.Brightness(image).enhance(1.0 + 0.8 * severity)
    if kind == "contrast":
        return ImageEnhance.Contrast(image).enhance(1.0 + severity)
    if kind == "blur":
        return image.filter(ImageFilter.GaussianBlur(radius=3.0 * severity))
    if kind == "jpeg":
        import io
        buffer = io.BytesIO()
        image.save(buffer, format="JPEG", quality=max(10, int(100 - 80 * severity)))
        buffer.seek(0)
        return Image.open(buffer).convert("RGB")
    if kind == "noise":
        rng = np.random.default_rng(seed)
        array = np.asarray(image.convert("RGB"), dtype=np.float32)
        array += rng.normal(0, 35 * severity, array.shape)
        return Image.fromarray(array.clip(0, 255).astype(np.uint8))
    raise ValueError(f"Unknown shift: {kind}")
