COUNTER = 0


def local_double(value):
    """
    Create a local variable containing value * 2 and return it.
    """
    result = value * 2
    return result


def read_limit(value, limit):
    """
    Return True if value is less than or equal to limit.
    """
    return value <= limit


def increment_global():
    """
    Increment the module-level COUNTER and return its new value.
    """
    global COUNTER
    COUNTER += 1
    return COUNTER


def mutate_shared(items, value):
    """
    Append value to the supplied list and return the same list.
    """
    items.append(value)
    return items
