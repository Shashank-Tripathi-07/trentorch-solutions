import numpy as np


def bce_loss(y: np.ndarray, yhat: np.ndarray) -> float:
    """
    Binary cross-entropy loss.

    y: true labels, shape (n,), each 0 or 1.
    yhat: predicted probabilities, shape (n,), guaranteed in [1e-7, 1 - 1e-7].

    L = -(1/n) * sum( y*log(yhat) + (1-y)*log(1-yhat) )

    yhat is already clamped away from 0 and 1 by the input guarantee, so no
    extra epsilon-clamping is needed.
    """
    y = np.asarray(y, dtype=np.float64)
    yhat = np.asarray(yhat, dtype=np.float64)

    losses = y * np.log(yhat) + (1.0 - y) * np.log1p(-yhat)
    return float(-np.mean(losses))
