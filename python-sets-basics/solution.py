def unique_values(values) -> set:
    """
    Return a set containing each distinct element.
    """
    return set(values)


def contains_all(values, candidates) -> bool:
    """
    Check whether all candidates exist in values.
    """
    values_set = set(values)

    return all(candidate in values_set for candidate in candidates)


def unique_count(values) -> int:
    """
    Return the number of distinct elements.
    """
    return len(set(values))


def add_values(values, additions) -> set:
    """
    Create a new set and add all supplied elements.
    """
    result = set(values)

    for value in additions:
        result.add(value)

    return result


def remove_if_present(values: set, value) -> set:
    """
    Remove an element if present, without raising an error.
    """
    values.discard(value)

    return values


def remove_required(values: set, value) -> set:
    """
    Remove an element, raising KeyError if absent.
    """
    values.remove(value)

    return values


def empty_set(values: set) -> set:
    """
    Remove all elements while preserving set identity.
    """
    values.clear()

    return values
