import math


def squares_of_evens(numbers: list) -> list:
    """
    Return squares of even numbers only.
    """
    return [n * n for n in numbers if n % 2 == 0]


def label_parity(numbers: list) -> list:
    """
    Label every number as even or odd.
    """
    return ["even" if n % 2 == 0 else "odd" for n in numbers]


def flatten(nested: list) -> list:
    """
    Flatten a list of lists using a nested comprehension.
    """
    return [item for inner_list in nested for item in inner_list]


def multiplication_table(n: int) -> list:
    """
    Generate an n-by-n multiplication table.
    """
    if n <= 0:
        return []

    return [
        [i * j for j in range(1, n + 1)]
        for i in range(1, n + 1)
    ]


def elementwise(func, *vectors) -> list:
    """
    Apply a function position-wise across multiple vectors.
    """
    if not vectors:
        return []

    return [func(*items) for items in zip(*vectors)]


def mask_select(values: list, mask: list) -> list:
    """
    Select values whose corresponding mask elements are truthy.
    """
    return [value for value, keep in zip(values, mask) if keep]


def broadcast_add(values: list, other) -> list:
    """
    Add another sequence element-wise or broadcast a scalar.
    """
    if hasattr(other, "__len__"):
        return [a + b for a, b in zip(values, other)]

    return [value + other for value in values]


def normalize(values: list, eps: float) -> list:
    """
    Perform layer normalization.
    """
    if not values:
        return []

    n = len(values)

    mean = sum(values) / n

    variance = sum((x - mean) ** 2 for x in values) / n

    denominator = math.sqrt(variance + eps)

    return [(x - mean) / denominator for x in values]
