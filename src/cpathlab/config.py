from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass(slots=True)
class DataConfig:
    image_dir: str = "data/example/images"
    labels_csv: str = "data/example/labels.csv"
    image_size: int = 96
    seed: int = 42
    val_fraction: float = 0.15
    test_fraction: float = 0.15


@dataclass(slots=True)
class ModelConfig:
    name: str = "baseline_cnn"
    num_classes: int = 2
    pretrained: bool = False
    dropout: float = 0.25


@dataclass(slots=True)
class TrainingConfig:
    epochs: int = 10
    batch_size: int = 32
    learning_rate: float = 1e-3
    weight_decay: float = 1e-4
    device: str = "auto"


@dataclass(slots=True)
class ExperimentConfig:
    data: DataConfig = field(default_factory=DataConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    training: TrainingConfig = field(default_factory=TrainingConfig)
    experiment_name: str = "cpathlab"

    @classmethod
    def from_yaml(cls, path: str | Path) -> ExperimentConfig:
        raw: dict[str, Any] = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
        return cls(
            data=DataConfig(**raw.get("data", {})),
            model=ModelConfig(**raw.get("model", {})),
            training=TrainingConfig(**raw.get("training", {})),
            experiment_name=raw.get("experiment_name", "cpathlab"),
        )
