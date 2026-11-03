def combine_sets(a: set, b: set) -> set:
    """Return the union of two sets."""
    return a | b


def common_values(a: set, b: set) -> set:
    """Return the intersection of two sets."""
    return a & b


def only_in_first(a: set, b: set) -> set:
    """Return elements present in a but not in b."""
    return a - b


def in_exactly_one(a: set, b: set) -> set:
    """Return the symmetric difference of two sets."""
    return a ^ b


def relationship(a: set, b: set) -> tuple:
    """Return subset, superset and disjoint relationships."""
    return (
        a.issubset(b),
        a.issuperset(b),
        a.isdisjoint(b)
    )
