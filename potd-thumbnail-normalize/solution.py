import numpy as np


def normalize_image(matrix: np.ndarray) -> tuple[float, float, np.ndarray]:
    m = np.asarray(matrix, dtype=np.float64)
    mu = float(m.mean())
    sigma = float(m.std())  # ddof=0 -> population std
    if sigma == 0.0:
        return mu, sigma, np.zeros_like(m)
    return mu, sigma, (m - mu) / sigma
