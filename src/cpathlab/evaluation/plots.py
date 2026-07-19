from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import ConfusionMatrixDisplay, PrecisionRecallDisplay, RocCurveDisplay


def save_evaluation_plots(y_true: np.ndarray, probabilities: np.ndarray, output_dir: str | Path, threshold: float = 0.5) -> list[Path]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    predictions = (probabilities >= threshold).astype(int)
    paths: list[Path] = []
    figures = [
        ("confusion_matrix.png", lambda: ConfusionMatrixDisplay.from_predictions(y_true, predictions)),
        ("roc_curve.png", lambda: RocCurveDisplay.from_predictions(y_true, probabilities)),
        ("precision_recall_curve.png", lambda: PrecisionRecallDisplay.from_predictions(y_true, probabilities)),
    ]
    for name, draw in figures:
        plt.figure()
        draw()
        path = output / name
        plt.savefig(path, bbox_inches="tight", dpi=160)
        plt.close()
        paths.append(path)
    return paths
