from __future__ import annotations

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: str
    model_status: str
    clinical_use: str = "prohibited"


class PredictionResponse(BaseModel):
    probability: float = Field(ge=0.0, le=1.0)
    predicted_label: int = Field(ge=0, le=1)
    confidence_band: str
    model_status: str
    disclaimer: str
