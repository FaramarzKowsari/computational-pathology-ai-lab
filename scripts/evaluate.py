from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from cpathlab.evaluation.metrics import classification_metrics
from cpathlab.evaluation.plots import save_evaluation_plots


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate saved arrays without inventing results")
    parser.add_argument("--labels", required=True, help=".npy file of binary labels")
    parser.add_argument("--probabilities", required=True, help=".npy file of positive-class probabilities")
    parser.add_argument("--output", default="reports/evaluation")
    args = parser.parse_args()
    labels = np.load(args.labels)
    probabilities = np.load(args.probabilities)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    metrics = classification_metrics(labels, probabilities)
    (output / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    save_evaluation_plots(labels, probabilities, output)
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
