import numpy as np

from cpathlab.monitoring.drift import population_stability_index


def test_psi_detects_change() -> None:
    rng = np.random.default_rng(1)
    reference = rng.normal(0, 1, 1000)
    same = rng.normal(0, 1, 1000)
    shifted = rng.normal(2, 1, 1000)
    assert population_stability_index(reference, shifted) > population_stability_index(reference, same)
