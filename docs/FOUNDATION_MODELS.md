# Foundation Model Integration

The repository provides an adapter boundary rather than redistributing third-party weights. To integrate a model:

1. Review the model card, access conditions, and license.
2. Download weights directly from the authorized source.
3. Wrap the encoder so it maps `[B, C, H, W]` to `[B, D]`.
4. Record the exact checkpoint hash and preprocessing.
5. Run frozen linear-probe and controlled fine-tuning experiments.
6. Never imply clinical equivalence based only on an internal patch benchmark.
