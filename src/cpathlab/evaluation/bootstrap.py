from __future__ import annotations

from collections.abc import Callable

import numpy as np


def bootstrap_interval(y_true: np.ndarray, scores: np.ndarray, metric: Callable[[np.ndarray, np.ndarray], float], samples: int = 1000, confidence: float = 0.95, seed: int = 42) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    values: list[float] = []
    for _ in range(samples):
        indices = rng.integers(0, len(y_true), len(y_true))
        try:
            value = float(metric(y_true[indices], scores[indices]))
            if np.isfinite(value):
                values.append(value)
        except ValueError:
            continue
    if not values:
        return float("nan"), float("nan")
    alpha = (1 - confidence) / 2
    return float(np.quantile(values, alpha)), float(np.quantile(values, 1 - alpha))
