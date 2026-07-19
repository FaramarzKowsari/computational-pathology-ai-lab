from __future__ import annotations

import numpy as np


def population_stability_index(reference: np.ndarray, current: np.ndarray, bins: int = 10) -> float:
    reference = np.asarray(reference, dtype=float).ravel()
    current = np.asarray(current, dtype=float).ravel()
    quantiles = np.asarray(np.quantile(reference, np.linspace(0, 1, bins + 1)), dtype=float)
    edges = np.concatenate((np.array([-np.inf]), quantiles[1:-1], np.array([np.inf])))
    expected = np.histogram(reference, bins=edges)[0] / len(reference)
    actual = np.histogram(current, bins=edges)[0] / len(current)
    expected = np.clip(expected, 1e-6, None)
    actual = np.clip(actual, 1e-6, None)
    return float(np.sum((actual - expected) * np.log(actual / expected)))


def image_channel_summary(batch: np.ndarray) -> dict[str, list[float]]:
    if batch.ndim != 4 or batch.shape[-1] != 3:
        raise ValueError("batch must have shape [N, H, W, 3]")
    return {
        "mean": batch.mean(axis=(0, 1, 2)).astype(float).tolist(),
        "std": batch.std(axis=(0, 1, 2)).astype(float).tolist(),
    }
