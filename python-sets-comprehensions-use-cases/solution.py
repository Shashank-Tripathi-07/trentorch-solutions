def squared_unique(values) -> set:
    """Return unique squares of all values."""
    return {value ** 2 for value in values}


def positive_unique(values) -> set:
    """Return distinct positive values."""
    return {value for value in values if value > 0}


def word_lengths(words: list) -> set:
    """Return unique word lengths."""
    return {len(word) for word in words}


def coordinate_sums(points: list) -> set:
    """Return unique sums of point coordinates."""
    return {x + y for x, y in points}


def find_duplicates(values: list) -> set:
    """Return all values that occur more than once."""
    seen = set()
    duplicates = set()

    for value in values:
        if value in seen:
            duplicates.add(value)
        else:
            seen.add(value)

    return duplicates


def unique_in_first_seen_order(values: list) -> list:
    """Return unique values while preserving their first appearance order."""
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


def all_seen_before(values: list) -> bool:
    """Return True if no value occurs exactly once."""
    seen = set()
    repeated = set()

    for value in values:
        if value in seen:
            repeated.add(value)
        else:
            seen.add(value)

    return seen == repeated


def missing_values(values: list, expected: set) -> set:
    """Return expected values that are absent from values."""
    return expected - set(values)
