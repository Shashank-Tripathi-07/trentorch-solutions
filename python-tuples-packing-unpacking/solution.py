def rotate_three(a, b, c) -> tuple:
    """
    Return a tuple (b, c, a) using multiple assignment.
    """
    a, b, c = b, c, a
    return (a, b, c)


def head_and_tail(seq) -> tuple:
    """
    Return the first element and a list of remaining elements.
    """
    if not seq:
        return (None, [])

    head, *tail = seq
    return (head, tail)


def ends_and_middle(seq) -> tuple:
    """
    Return the first element, middle elements, and last element.
    """
    first, *middle, last = seq
    return (first, middle, last)


def sum_pairs(pairs: list) -> list:
    """
    Return the sum of each pair.
    """
    result = []

    for a, b in pairs:
        result.append(a + b)

    return result
