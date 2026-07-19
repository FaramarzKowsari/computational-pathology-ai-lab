from __future__ import annotations

import io
import os
from functools import lru_cache
from typing import Annotated

from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError

from cpathlab.inference.predictor import DemoPredictor, Predictor

from .schemas import HealthResponse, PredictionResponse

app = FastAPI(
    title="Computational Pathology AI Lab API",
    version="1.0.0",
    description="Research-only image inference API. Not a medical device and not for clinical use.",
)


@lru_cache
def get_predictor() -> Predictor | DemoPredictor:
    model_path = os.getenv("CPATHLAB_MODEL_PATH")
    if model_path and os.path.exists(model_path):
        return Predictor.from_checkpoint(model_path)
    if os.getenv("CPATHLAB_ALLOW_DEMO_PREDICTOR", "true").lower() == "true":
        return DemoPredictor()
    raise RuntimeError("No checkpoint configured and demo predictor is disabled")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    predictor = get_predictor()
    status = getattr(predictor, "model_status", predictor.__class__.__name__)
    return HealthResponse(status="ok", model_status=str(status))


@app.post("/predict", response_model=PredictionResponse)
async def predict(file: Annotated[UploadFile, File()]) -> PredictionResponse:
    if file.content_type not in {"image/png", "image/jpeg", "image/tiff"}:
        raise HTTPException(status_code=415, detail="Supported formats: PNG, JPEG, TIFF")
    content = await file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="Image exceeds 10 MB")
    try:
        image = Image.open(io.BytesIO(content)).convert("RGB")
    except UnidentifiedImageError as exc:
        raise HTTPException(status_code=400, detail="Invalid image") from exc
    result = get_predictor().predict(image)
    return PredictionResponse(
        probability=result.probability,
        predicted_label=result.predicted_label,
        confidence_band=result.confidence_band,
        model_status=result.model_status,
        disclaimer="Research demonstration only. Not validated for clinical diagnosis or patient care.",
    )
