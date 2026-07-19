# Architecture

The platform separates data, modeling, evidence, and delivery. This prevents notebook state from becoming the only record of an experiment.

1. **Data plane:** validation, group-aware splitting, preprocessing, synthetic fixtures, WSI thumbnails, tissue masking, and patch extraction.
2. **Model plane:** baseline CNN, transfer learning, tiny ViT, external foundation adapters, and attention MIL.
3. **Evidence plane:** discrimination, calibration, confidence intervals, error tables, explainability, uncertainty, and domain-shift probes.
4. **Operations plane:** configuration, CLI, tests, CI, DVC, MLflow hooks, model registry, API, container, and monitoring.
5. **Knowledge plane:** notebooks, model/data cards, research questions, technical report, companion book, and website.

See `docs/assets/architecture.svg` for the visual system map.
