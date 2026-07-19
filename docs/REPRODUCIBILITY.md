# Reproducibility Guide

1. Create an isolated Python 3.11+ environment.
2. Install `pip install -e ".[dev]"`.
3. Record `python --version`, `pip freeze`, hardware, seed, dataset checksum, and git commit.
4. Run `cpathlab validate-data` before training.
5. Generate split manifests once and version them.
6. Run tests and archive logs.
7. Store weights, metrics, plots, and configuration together.
8. Register a release only after the README evidence matches the generated artifacts.

The repository's committed example data are synthetic and should never be interpreted as clinical evidence.
