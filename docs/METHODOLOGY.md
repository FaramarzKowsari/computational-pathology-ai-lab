# Methodology

## Primary research question
How do conventional CNNs, modern vision architectures, and legally obtained pathology foundation encoders compare under controlled label budgets, leakage-resistant splits, calibration analysis, and domain shifts?

## Mandatory controls
- Define the patient/slide as the split unit.
- Freeze a final test set before model selection.
- Use identical preprocessing and label budgets where scientifically appropriate.
- Tune thresholds on validation data only.
- Report point estimates with bootstrap confidence intervals.
- Audit false negatives separately.
- Record compute, random seeds, package versions, and failed runs.

## Benchmark matrix
The templates cover baseline CNN, ResNet, DenseNet, EfficientNet, ConvNeXt, tiny ViT, external foundation adapters, and MIL. No row receives a score until the corresponding run artifacts exist.
