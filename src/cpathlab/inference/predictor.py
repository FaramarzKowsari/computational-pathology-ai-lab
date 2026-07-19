from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import torch
from PIL import Image
from torch import nn

from cpathlab.data.preprocessing import image_to_tensor
from cpathlab.models import create_model


@dataclass(slots=True)
class Prediction:
    probability: float
    predicted_label: int
    confidence_band: str
    model_status: str


class Predictor:
    def __init__(self, model: nn.Module, device: str = "cpu", model_status: str = "trained checkpoint") -> None:
        self.device = torch.device(device)
        self.model = model.to(self.device).eval()
        self.model_status = model_status

    @classmethod
    def from_checkpoint(cls, path: str | Path, model_name: str = "baseline_cnn", device: str = "cpu") -> Predictor:
        model = create_model(model_name)
        state = torch.load(path, map_location=device, weights_only=True)
        model.load_state_dict(state)
        return cls(model, device=device)

    @torch.inference_mode()
    def predict(self, image: Image.Image) -> Prediction:
        tensor = image_to_tensor(image).unsqueeze(0).to(self.device)
        probability = float(torch.softmax(self.model(tensor), dim=1)[0, 1].cpu())
        if 0.4 <= probability <= 0.6:
            band = "uncertain - research review recommended"
        elif probability > 0.6:
            band = "higher model score"
        else:
            band = "lower model score"
        return Prediction(probability, int(probability >= 0.5), band, self.model_status)


class DemoPredictor:
    """Deterministic non-medical placeholder used only when explicitly enabled."""
    def predict(self, image: Image.Image) -> Prediction:
        import numpy as np
        array = np.asarray(image.convert("RGB"), dtype=np.float32)
        purple_density = float(np.mean(array[..., 2] - array[..., 1]))
        probability = float(1 / (1 + np.exp(-purple_density / 25)))
        return Prediction(probability, int(probability >= 0.5), "synthetic demo score", "DEMO PREDICTOR - NOT A TRAINED MEDICAL MODEL")
