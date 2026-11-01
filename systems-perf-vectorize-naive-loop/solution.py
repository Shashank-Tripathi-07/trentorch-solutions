import time
import numpy as np


def naive_dot_product(a: list, b: list) -> float:
    """
    a, b: plain Python lists of equal length
    """
    total = 0.0

    for x, y in zip(a, b):
        total += x * y

    return total


def vectorized_dot_product(a: np.ndarray, b: np.ndarray) -> float:
    """
    a, b: NumPy arrays of equal length
    """
    return float(np.dot(a, b))


def compare_speed(a: np.ndarray, b: np.ndarray) -> dict:
    """
    Runs both implementations, measures execution time,
    and returns their results and speedup.
    """

    # Convert NumPy arrays into Python lists
    a_list = a.tolist()
    b_list = b.tolist()

    # Time naive implementation
    start = time.perf_counter()
    naive_result = naive_dot_product(a_list, b_list)
    naive_time = time.perf_counter() - start

    # Time vectorized implementation
    start = time.perf_counter()
    vectorized_result = vectorized_dot_product(a, b)
    vectorized_time = time.perf_counter() - start

    # Calculate speedup
    speedup = naive_time / vectorized_time if vectorized_time > 0 else float('inf')

    return {
        "naive_result": naive_result,
        "vectorized_result": vectorized_result,
        "naive_time": naive_time,
        "vectorized_time": vectorized_time,
        "speedup": speedup
    }
