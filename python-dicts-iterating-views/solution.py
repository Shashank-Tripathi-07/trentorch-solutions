def sum_of_values(d: dict) -> int:
    """
    Return the sum of all dictionary values.
    """
    return sum(d.values())


def keys_with_max_value(d: dict) -> list:
    """
    Return all keys whose values equal the maximum value.
    """
    if not d:
        return []

    maximum = max(d.values())

    return [
        key
        for key, value in d.items()
        if value == maximum
    ]


def remove_where_value_below(d: dict, threshold: int) -> None:
    """
    Remove entries whose values are below the threshold.
    """
    for key, value in list(d.items()):
        if value < threshold:
            del d[key]


def value_of(pair: tuple):
    """
    Return the value from a key-value pair.
    """
    return pair[1]


def items_by_value_desc(d: dict) -> list:
    """
    Sort dictionary entries by value descending,
    with keys ascending for ties.
    """
    result = sorted(d.items())
    result = sorted(result, key=value_of, reverse=True)

    return result
