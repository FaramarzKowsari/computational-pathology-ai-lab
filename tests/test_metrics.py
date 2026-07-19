import numpy as np

from cpathlab.evaluation.bootstrap import bootstrap_interval
from cpathlab.evaluation.metrics import classification_metrics


def test_metrics_are_bounded() -> None:
    labels = np.array([0, 0, 1, 1])
    probabilities = np.array([0.1, 0.4, 0.6, 0.9])
    metrics = classification_metrics(labels, probabilities)
    for key in ["roc_auc", "pr_auc", "sensitivity", "specificity", "f1", "balanced_accuracy", "brier_score", "ece"]:
        assert 0 <= metrics[key] <= 1


def test_bootstrap_interval() -> None:
    labels = np.array([0, 0, 1, 1, 0, 1])
    scores = np.array([0.1, 0.2, 0.8, 0.9, 0.3, 0.7])
    low, high = bootstrap_interval(labels, scores, lambda y, s: float(np.mean((s >= 0.5) == y)), samples=50)
    assert low <= high
