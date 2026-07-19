from __future__ import annotations

import torch
from torch import nn


class TemperatureScaler(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.log_temperature = nn.Parameter(torch.zeros(1))

    @property
    def temperature(self) -> torch.Tensor:
        return self.log_temperature.exp().clamp(0.05, 20.0)

    def forward(self, logits: torch.Tensor) -> torch.Tensor:
        return logits / self.temperature

    def fit(self, logits: torch.Tensor, labels: torch.Tensor, steps: int = 100, learning_rate: float = 0.05) -> float:
        optimizer = torch.optim.LBFGS([self.log_temperature], lr=learning_rate, max_iter=steps)
        criterion = nn.CrossEntropyLoss()
        def closure() -> torch.Tensor:
            optimizer.zero_grad()
            loss = criterion(self(logits), labels)
            loss.backward()
            return loss
        optimizer.step(closure)
        return float(self.temperature.detach())
