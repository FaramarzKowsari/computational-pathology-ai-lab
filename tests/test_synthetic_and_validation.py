from pathlib import Path

from cpathlab.data.synthetic import generate_synthetic_dataset
from cpathlab.data.validation import validate_dataset


def test_generate_and_validate(tmp_path: Path) -> None:
    manifest = generate_synthetic_dataset(tmp_path, samples=12, seed=7)
    report = validate_dataset(tmp_path / "images", manifest)
    assert report.ok
    assert report.valid_images == 12
