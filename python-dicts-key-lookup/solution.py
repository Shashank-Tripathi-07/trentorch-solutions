def first_positions(words: list) -> dict:
    """
    Map each distinct word to the index of its first occurrence.
    """
    positions = {}

    for index, word in enumerate(words):
        if word not in positions:
            positions[word] = index

    return positions


def same_key(a, b) -> bool:
    """
    Check whether two hashable objects behave as the same dictionary key.
    """
    return hash(a) == hash(b) and a == b


def distinct_key_count(keys: list) -> int:
    """
    Count distinct dictionary keys.
    """
    result = {}

    for key in keys:
        result[key] = None

    return len(result)
