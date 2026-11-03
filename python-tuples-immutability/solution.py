def make_singleton(x) -> tuple:
    """Return a tuple containing exactly one element."""
    return (x,)


def tuple_replace(t: tuple, index: int, value) -> tuple:
    """Return a new tuple with the element at index replaced."""
    if index < -len(t) or index >= len(t):
        return t

    if index < 0:
        index += len(t)

    return t[:index] + (value,) + t[index + 1:]


def count_and_first_index(t: tuple, x) -> tuple:
    """Return the count and first index of x in t."""
    count = t.count(x)

    if x in t:
        first_index = t.index(x)
    else:
        first_index = -1

    return (count, first_index)


def freeze_rows(matrix: list) -> tuple:
    """Convert a list of lists into a tuple of tuples."""
    return tuple(tuple(row) for row in matrix)


def thaw_rows(frozen: tuple) -> list:
    """Convert a tuple of tuples into a list of lists."""
    return [list(row) for row in frozen]


def updated(seq, index: int, value):
    """Return a new sequence of the same type with one element updated."""
    if isinstance(seq, list):
        result = seq.copy()

        if -len(result) <= index < len(result):
            result[index] = value

        return result

    elif isinstance(seq, tuple):
        return tuple_replace(seq, index, value)

    else:
        raise TypeError("seq must be a list or tuple")


def has_mutable_element(t: tuple) -> bool:
    """Check whether any direct element is a list, dict, or set."""
    return any(
        isinstance(item, (list, dict, set))
        for item in t
    )
