# Model Registry

Do not commit unrestricted model weights by default. Each registered model should have a folder containing:

- `metadata.json`
- configuration
- training-data reference and checksum
- evaluation report
- model-card addendum
- checkpoint checksum and authorized storage location
- approval status: `research-only`, `rejected`, or `archived`

No model in this initial release has clinical approval.
