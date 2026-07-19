# MLOps Design

- **Configuration:** YAML and typed dataclasses.
- **Data versioning:** DVC stages and immutable manifests.
- **Experiment tracking:** optional MLflow tracker.
- **Registry:** `model_registry/` stores review metadata, not unrestricted weights.
- **CI:** tests, lint, and container build.
- **Serving:** FastAPI with health and prediction endpoints.
- **Monitoring:** input summaries, PSI drift, confidence distribution, latency, and failure counts.
- **Release evidence:** generated test report, checksum manifest, model/data cards, and changelog.
