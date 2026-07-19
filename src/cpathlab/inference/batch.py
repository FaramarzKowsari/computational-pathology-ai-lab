from __future__ import annotations

from dataclasses import asdict
from pathlib import Path

import pandas as pd
from PIL import Image

from .predictor import Predictor


def batch_predict(predictor: Predictor, paths: list[str | Path]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for raw in paths:
        path = Path(raw)
        with Image.open(path) as image:
            prediction = predictor.predict(image.copy())
        rows.append({"image": str(path), **asdict(prediction)})
    return pd.DataFrame(rows)
