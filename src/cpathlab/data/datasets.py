from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pandas as pd
import torch
from PIL import Image
from torch.utils.data import Dataset

from .preprocessing import image_to_tensor


class PatchDataset(Dataset[tuple[torch.Tensor, torch.Tensor]]):
    def __init__(
        self,
        manifest: str | Path | pd.DataFrame,
        image_dir: str | Path,
        transform: Callable[[Image.Image], torch.Tensor] | None = None,
    ) -> None:
        self.frame = pd.read_csv(manifest) if not isinstance(manifest, pd.DataFrame) else manifest.copy()
        self.image_dir = Path(image_dir)
        self.transform = transform or image_to_tensor

    def __len__(self) -> int:
        return len(self.frame)

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        row = self.frame.iloc[index]
        with Image.open(self.image_dir / str(row["image"])) as image:
            tensor = self.transform(image.copy())
        label = torch.tensor(int(row["label"]), dtype=torch.long)
        return tensor, label
