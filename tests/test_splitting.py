import pandas as pd

from cpathlab.data.splitting import split_manifest


def test_group_split_has_no_overlap() -> None:
    frame = pd.DataFrame({"image": [f"x{i}.png" for i in range(40)], "label": [i % 2 for i in range(40)], "group": [f"g{i//4}" for i in range(40)]})
    result = split_manifest(frame, seed=3)
    groups = {name: set(result.loc[result.split == name, "group"]) for name in ["train", "val", "test"]}
    assert groups["train"].isdisjoint(groups["val"])
    assert groups["train"].isdisjoint(groups["test"])
    assert groups["val"].isdisjoint(groups["test"])
