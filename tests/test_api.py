import io

from fastapi.testclient import TestClient
from PIL import Image

from cpathlab.api.main import app, get_predictor


def test_health_and_predict() -> None:
    get_predictor.cache_clear()
    client = TestClient(app)
    health = client.get("/health")
    assert health.status_code == 200
    image = Image.new("RGB", (96, 96), (170, 100, 190))
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    response = client.post("/predict", files={"file": ("patch.png", buffer.getvalue(), "image/png")})
    assert response.status_code == 200
    assert "Not a trained medical model" in response.json()["model_status"].title() or "DEMO" in response.json()["model_status"]
