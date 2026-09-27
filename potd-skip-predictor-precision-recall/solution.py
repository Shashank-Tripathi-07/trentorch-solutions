import numpy as np


def precision_recall_f1(p: np.ndarray, y: np.ndarray) -> tuple[float, float, float]:
    """
    Precision, recall, and F1 for binary predictions p against labels y.

    p, y: shape (n,), each entry 0 or 1.

    precision = TP / (TP + FP), recall = TP / (TP + FN),
    f1 = 2 * precision * recall / (precision + recall).

    If a denominator is 0 (no predicted positives for precision, no actual
    positives for recall), report 0.0 for that metric instead of crashing.
    """
    p = np.asarray(p).astype(bool)
    y = np.asarray(y).astype(bool)

    tp = int(np.count_nonzero(p & y))
    fp = int(np.count_nonzero(p & ~y))
    fn = int(np.count_nonzero(~p & y))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = (2 * precision * recall / (precision + recall)
          if (precision + recall) > 0 else 0.0)

    return float(precision), float(recall), float(f1)
