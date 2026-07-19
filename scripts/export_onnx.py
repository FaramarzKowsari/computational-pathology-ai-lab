from __future__ import annotations

import argparse
from pathlib import Path

import torch

from cpathlab.models import create_model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint", required=True)
    parser.add_argument("--model", default="baseline_cnn")
    parser.add_argument("--output", default="models/model.onnx")
    parser.add_argument("--image-size", type=int, default=96)
    args = parser.parse_args()
    model = create_model(args.model).eval()
    state = torch.load(args.checkpoint, map_location="cpu", weights_only=True)
    model.load_state_dict(state)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    dummy = torch.randn(1, 3, args.image_size, args.image_size)
    torch.onnx.export(model, dummy, output, input_names=["image"], output_names=["logits"], dynamic_axes={"image": {0: "batch"}, "logits": {0: "batch"}}, opset_version=17)
    print(output)


if __name__ == "__main__":
    main()
