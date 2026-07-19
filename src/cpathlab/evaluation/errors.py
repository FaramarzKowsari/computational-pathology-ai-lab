from __future__ import annotations

import numpy as np
import pandas as pd


def error_table(ids: list[str], y_true: np.ndarray, probabilities: np.ndarray, threshold: float = 0.5) -> pd.DataFrame:
    predictions = (probabilities >= threshold).astype(int)
    frame = pd.DataFrame({"id": ids, "label": y_true, "probability": probabilities, "prediction": predictions})
    frame["error_type"] = np.select(
        [(frame.label == 1) & (frame.prediction == 0), (frame.label == 0) & (frame.prediction == 1)],
        ["false_negative", "false_positive"],
        default="correct",
    )
    frame["uncertainty"] = 1.0 - np.abs(frame["probability"] - 0.5) * 2
    return frame.sort_values(["error_type", "uncertainty"], ascending=[True, False])
