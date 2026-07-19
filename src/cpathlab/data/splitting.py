from __future__ import annotations

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit, train_test_split


def split_manifest(
    frame: pd.DataFrame,
    val_fraction: float = 0.15,
    test_fraction: float = 0.15,
    seed: int = 42,
    group_column: str | None = "group",
) -> pd.DataFrame:
    """Return a copy with a leakage-aware `split` column."""
    if val_fraction <= 0 or test_fraction <= 0 or val_fraction + test_fraction >= 1:
        raise ValueError("val_fraction and test_fraction must be positive and sum to less than 1")
    result = frame.copy().reset_index(drop=True)
    result["split"] = "train"
    if group_column and group_column in result.columns:
        outer = GroupShuffleSplit(n_splits=1, test_size=val_fraction + test_fraction, random_state=seed)
        train_idx, hold_idx = next(outer.split(result, result["label"], result[group_column]))
        hold = result.iloc[hold_idx]
        relative_test = test_fraction / (val_fraction + test_fraction)
        inner = GroupShuffleSplit(n_splits=1, test_size=relative_test, random_state=seed + 1)
        val_rel, test_rel = next(inner.split(hold, hold["label"], hold[group_column]))
        result.loc[result.index[train_idx], "split"] = "train"
        result.loc[hold.index[val_rel], "split"] = "val"
        result.loc[hold.index[test_rel], "split"] = "test"
    else:
        train_idx, hold_idx = train_test_split(
            result.index,
            test_size=val_fraction + test_fraction,
            stratify=result["label"],
            random_state=seed,
        )
        relative_test = test_fraction / (val_fraction + test_fraction)
        val_idx, test_idx = train_test_split(
            hold_idx,
            test_size=relative_test,
            stratify=result.loc[hold_idx, "label"],
            random_state=seed + 1,
        )
        result.loc[train_idx, "split"] = "train"
        result.loc[val_idx, "split"] = "val"
        result.loc[test_idx, "split"] = "test"
    return result
