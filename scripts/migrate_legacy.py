from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "legacy" / "cu_boulder_original_assignment"
CANDIDATES = [
    "cnn-histopathologic-cancer-detection-colorado boulder university Assignment.ipynb",
    "cnn-histopathologic-cancer-detection-colorado.ipynb",
    "submission.csv",
    "kaggle_leaderboard_submission.jpg",
]


def main() -> None:
    TARGET.mkdir(parents=True, exist_ok=True)
    moved: list[str] = []
    for name in CANDIDATES:
        source = ROOT / name
        destination = TARGET / name
        if source.exists() and source.resolve() != destination.resolve():
            if destination.exists():
                print(f"Skipped existing legacy file: {destination.relative_to(ROOT)}")
                continue
            shutil.move(str(source), str(destination))
            moved.append(name)
            print(f"Moved {name} -> {destination.relative_to(ROOT)}")
    manifest = TARGET / "migration-result.json"
    manifest.write_text(json.dumps({"moved": moved, "source_repository": "Deep-Learning-Cancer-Detection-CU-Boulder"}, indent=2), encoding="utf-8")
    if not moved:
        print("No original root files were found. They may already be migrated. See legacy/README.md.")


if __name__ == "__main__":
    main()
