import torch

from cpathlab.explainability.gradcam import GradCAM
from cpathlab.explainability.integrated_gradients import integrated_gradients
from cpathlab.models import BaselineCNN


def test_gradcam_and_integrated_gradients() -> None:
    model = BaselineCNN()
    image = torch.randn(1, 3, 32, 32)
    cam = GradCAM(model, model.features[8])(image)
    assert cam.shape == (1, 1, 32, 32)
    attribution = integrated_gradients(model, image, target=1, steps=2)
    assert attribution.shape == image.shape
