def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it.
    """
    if value is None:
        return False

    elif isinstance(value, (int, float, complex)):
        return value != 0

    elif isinstance(value, str):
        return len(value) > 0

    elif isinstance(value, (list, tuple, dict, set, frozenset)):
        return len(value) > 0

    else:
        return True


def first_truthy(values: list):
    """
    Return the first truthy value in the list.
    If none is truthy, return None.
    """
    for value in values:
        if is_truthy(value):
            return value

    return None
