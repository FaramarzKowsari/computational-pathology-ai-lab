# Benchmark Protocol

## Status
**Not Yet Benchmarked on the real histopathology dataset.**

## Required table columns
Model, checkpoint source, trainable parameters, label budget, split unit, seed, ROC-AUC, PR-AUC, sensitivity, specificity, F1, MCC, Brier score, ECE, latency, memory, and confidence interval.

## Anti-fabrication rule
A result may enter `reports/benchmark_results.csv` only when its configuration, log, predictions, and checkpoint checksum are archived. Missing experiments remain blank and carry `Not Yet Benchmarked`.
