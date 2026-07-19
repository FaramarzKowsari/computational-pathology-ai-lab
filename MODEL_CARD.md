# Model Card

## Model family
This repository contains research implementations and adapters rather than a single clinically released model.

## Intended use
- Education, reproducible experimentation, software engineering demonstrations, and non-clinical research.
- Binary classification of synthetic or properly licensed histology patches after explicit training.

## Out-of-scope use
- Clinical diagnosis, triage, treatment selection, prognosis, or autonomous medical decision-making.
- Processing identifiable patient information in the public demo.

## Current evidence
- Unit tests and CPU smoke tests: available in `reports/TEST_REPORT.md`.
- Real histopathology benchmark: **Not Yet Benchmarked in this release**.
- External validation: **Not Yet Performed**.
- Clinical validation: **Not Performed**.

## Risks
Dataset shift, staining differences, scanner variation, label noise, shortcut learning, demographic imbalance, and poorly calibrated confidence can cause harmful errors.

## Required evaluation before research use
Report ROC-AUC, PR-AUC, sensitivity, specificity, F1, balanced accuracy, MCC, Brier score, calibration error, confidence intervals, subgroup analysis, and external validation.
