def square(x):
    """
    Return the square of x.

    Example:
        square(5) -> 25
    """
    return x ** 2


def min_max(values):
    """
    Return a tuple containing the minimum and maximum values.

    Example:
        min_max([4, 1, 7, 2]) -> (1, 7)
    """
    minimum = maximum = values[0]

    for value in values[1:]:
        if value < minimum:
            minimum = value

        if value > maximum:
            maximum = value

    return (minimum, maximum)


def describe_pair(a, b):
    """
    Return (sum, difference, product).
    """
    return (a + b, a - b, a * b)


def absolute_value(x):
    """
    Return the absolute value without using abs().
    """
    if x < 0:
        return -x

    return x


def percentage(value: float, total: float) -> float:
    """
    Return value as a percentage of total.
    """
    return (value / total) * 100


def repeat_text(text: str, count: int) -> str:
    """
    Return text repeated count times.
    """
    return text * count


def make_pair(first, second) -> tuple:
    """
    Return a tuple containing two values.
    """
    return (first, second)


def function_metadata():
    """
    Return this function's docstring and annotations.
    """
    return {
        "doc": function_metadata.__doc__,
        "annotations": function_metadata.__annotations__
    }
