from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd
from PIL import Image


@dataclass(slots=True)
class ValidationReport:
    total_rows: int
    valid_images: int
    missing_images: list[str]
    corrupt_images: list[str]
    duplicate_rows: int
    invalid_labels: list[str]

    @property
    def ok(self) -> bool:
        return not self.missing_images and not self.corrupt_images and not self.invalid_labels

    def to_dict(self) -> dict[str, object]:
        return asdict(self) | {"ok": self.ok}


def validate_dataset(image_dir: str | Path, labels_csv: str | Path) -> ValidationReport:
    image_root = Path(image_dir)
    frame = pd.read_csv(labels_csv)
    required = {"image", "label"}
    missing_columns = required.difference(frame.columns)
    if missing_columns:
        raise ValueError(f"Missing columns: {sorted(missing_columns)}")
    missing: list[str] = []
    corrupt: list[str] = []
    valid = 0
    for name in frame["image"].astype(str):
        path = image_root / name
        if not path.exists():
            missing.append(name)
            continue
        try:
            with Image.open(path) as image:
                image.verify()
            valid += 1
        except Exception:
            corrupt.append(name)
    invalid_labels = [str(v) for v in frame.loc[~frame["label"].isin([0, 1]), "label"].tolist()]
    return ValidationReport(
        total_rows=len(frame),
        valid_images=valid,
        missing_images=missing,
        corrupt_images=corrupt,
        duplicate_rows=int(frame.duplicated(subset=["image"]).sum()),
        invalid_labels=invalid_labels,
    )
