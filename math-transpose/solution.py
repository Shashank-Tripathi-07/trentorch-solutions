import numpy as np
from numpy.lib.stride_tricks import as_strided


def transpose(x: np.ndarray) -> np.ndarray:
    """
    Mirrors x.T: flips a matrix over its diagonal, so entry (i, j)
    becomes (j, i) and an (m, n) matrix becomes (n, m).
    """
    # Same buffer, reversed shape and strides: no data is copied.
    return as_strided(x, shape=x.shape[::-1], strides=x.strides[::-1])


def is_a_view_of(original: np.ndarray, derived: np.ndarray) -> bool:
    """True iff `derived` and `original` share memory."""
    return np.shares_memory(original, derived)
