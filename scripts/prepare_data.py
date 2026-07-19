from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from cpathlab.config import ExperimentConfig
from cpathlab.data.splitting import split_manifest
from cpathlab.data.validation import validate_dataset


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    config = ExperimentConfig.from_yaml(args.config)
    report = validate_dataset(config.data.image_dir, config.data.labels_csv)
    if not report.ok:
        raise SystemExit(report.to_dict())
    frame = pd.read_csv(config.data.labels_csv)
    split = split_manifest(frame, config.data.val_fraction, config.data.test_fraction, config.data.seed)
    output = Path("data/processed")
    output.mkdir(parents=True, exist_ok=True)
    split.to_csv(output / "manifest.csv", index=False)
    print(report.to_dict())


if __name__ == "__main__":
    main()
