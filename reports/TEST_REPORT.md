# Verified Test Report

Build date: 2026-07-19

## Automated tests

Command:

```bash
PYTHONPATH=src pytest -q --disable-warnings
```

Result:

```text
11 passed in 24.26s
```

Coverage of the test suite includes:

- synthetic image generation and dataset validation;
- leakage-resistant group splitting;
- baseline CNN, tiny Vision Transformer, ResNet, and attention MIL forward passes;
- ROC/PR and calibration-oriented metric computation;
- bootstrap confidence intervals;
- Grad-CAM and integrated gradients;
- population-stability drift detection;
- FastAPI health and image-prediction integration.

## Static quality checks

```text
Ruff: All checks passed.
MyPy: Success - no issues found in 42 source files.
Python compileall: completed without syntax errors.
```

MyPy was run with `--follow-imports=skip` so third-party deep-learning stubs do not dominate analysis; all project source files were checked.

## Data validation

The committed synthetic fixture was validated:

```json
{
  "total_rows": 24,
  "valid_images": 24,
  "missing_images": [],
  "corrupt_images": [],
  "duplicate_rows": 0,
  "invalid_labels": [],
  "ok": true
}
```

## CPU smoke training

A one-epoch CPU smoke training completed successfully. Its printed values are intentionally labeled **SYNTHETIC SMOKE METRICS - NOT A MEDICAL BENCHMARK**. They are not stored as scientific benchmark results and must not be cited as evidence of cancer-detection performance.

## Package build

The source distribution and wheel were built successfully with `python -m build`. Build products were removed from the repository package after verification to keep the Git history clean.

## PDF verification

`book/computational-pathology-engineering.pdf`:

- 8 A4 pages;
- opens successfully;
- not encrypted;
- text-based, not scanned;
- rendered at 150 DPI and visually inspected;
- a detected table-overflow issue on page 8 was corrected and re-rendered.

## Legacy migration test

The migration script was tested in a temporary repository. It moved matching original filenames into `legacy/cu_boulder_original_assignment/` and wrote `migration-result.json`.
