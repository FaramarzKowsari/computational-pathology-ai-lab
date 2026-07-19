import torch

from cpathlab.models import AttentionMIL, BaselineCNN, TinyVisionTransformer, create_model


def test_baseline_shape() -> None:
    assert BaselineCNN()(torch.randn(1, 3, 32, 32)).shape == (1, 2)


def test_vit_shape() -> None:
    assert TinyVisionTransformer(image_size=32, patch_size=8, dim=32, depth=1, heads=4)(torch.randn(1, 3, 32, 32)).shape == (1, 2)


def test_mil_shape() -> None:
    logits, attention = AttentionMIL(64)(torch.randn(2, 10, 64))
    assert logits.shape == (2, 2)
    assert attention.shape == (2, 10)
    assert torch.allclose(attention.sum(dim=1), torch.ones(2), atol=1e-5)


def test_factory_transfer_model() -> None:
    model = create_model("resnet18", pretrained=False).eval()
    assert model(torch.randn(1, 3, 32, 32)).shape == (1, 2)
