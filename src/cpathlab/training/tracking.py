from __future__ import annotations

from contextlib import AbstractContextManager
from dataclasses import dataclass, field
from typing import Any


@dataclass
class MemoryTracker(AbstractContextManager["MemoryTracker"]):
    params: dict[str, Any] = field(default_factory=dict)
    metrics: dict[str, float] = field(default_factory=dict)

    def __enter__(self) -> MemoryTracker:
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def log_params(self, values: dict[str, Any]) -> None:
        self.params.update(values)

    def log_metrics(self, values: dict[str, float]) -> None:
        self.metrics.update(values)


class MLflowTracker(AbstractContextManager["MLflowTracker"]):
    def __init__(self, experiment_name: str) -> None:
        try:
            import mlflow
        except ImportError as exc:
            raise RuntimeError("Install the mlops extra to use MLflow") from exc
        self.mlflow = mlflow
        self.mlflow.set_experiment(experiment_name)
        self.run: Any = None

    def __enter__(self) -> MLflowTracker:
        self.run = self.mlflow.start_run()
        return self

    def __exit__(self, *args: object) -> None:
        self.mlflow.end_run()

    def log_params(self, values: dict[str, Any]) -> None:
        self.mlflow.log_params(values)

    def log_metrics(self, values: dict[str, float]) -> None:
        self.mlflow.log_metrics(values)
