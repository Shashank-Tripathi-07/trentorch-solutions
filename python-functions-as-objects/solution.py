def alias_and_call(function, value):
    """
    Assign the function to a local alias and call it.
    """
    alias = function
    return alias(value)


def apply_selected(functions: list, index: int, value):
    """
    Select and call a function from a list.
    """
    selected_function = functions[index]
    return selected_function(value)


def same_function(function_a, function_b) -> bool:
    """
    Check whether both variables reference the same function object.
    """
    return function_a is function_b


def apply_once(function, value):
    """
    Call the supplied function once.
    """
    return function(value)


def apply_twice(function, value):
    """
    Apply the supplied function twice.
    """
    return function(function(value))


def apply_n_times(function, value, count: int):
    """
    Apply the supplied function count times.
    """
    for _ in range(count):
        value = function(value)

    return value


def transform_all(values: list, function) -> list:
    """
    Apply a function to every element and return a new list.
    """
    return [function(value) for value in values]


def make_square_function():
    """
    Return a lambda function that squares its input.
    """
    return lambda x: x ** 2


def make_offset_function(offset):
    """
    Return a lambda function that adds the supplied offset.
    """
    return lambda x: x + offset


def apply_lambda(values: list, function) -> list:
    """
    Apply a supplied function to every element.
    """
    return [function(value) for value in values]
