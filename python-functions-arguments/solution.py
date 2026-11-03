def build_point(x, y):
    """
    Return a 2-element tuple (x, y).
    """
    return (x, y)


def configure_model(name, dimensions, metric):
    """
    Return a dictionary containing model configuration.
    """
    return {
        "name": name,
        "dimensions": dimensions,
        "metric": metric
    }


def format_record(identifier, value, label):
    """
    Return a formatted record string.
    """
    return f"{identifier}={value} [{label}]"


def power(x, exponent=2):
    """
    Return x raised to exponent.
    """
    return x ** exponent


def make_label(value, prefix="item"):
    """
    Return a string in the form prefix:value.
    """
    return f"{prefix}:{value}"


def append_value(value, items=None):
    """
    Append value to items, creating a new list if necessary.
    """
    if items is None:
        items = []

    items.append(value)
    return items


def describe_config(name, enabled=True, retries=3):
    """
    Return (name, enabled, retries).
    """
    return (name, enabled, retries)


def sum_all(*values):
    """
    Return the sum of all positional arguments.
    """
    return sum(values)


def collect_types(*values):
    """
    Return the types of all positional arguments.
    """
    return tuple(type(value) for value in values)


def build_options(**options):
    """
    Return a new dictionary containing supplied keyword arguments.
    """
    return dict(options)


def summarize(required, *values, **options):
    """
    Return required, extra positional values, and keyword options.
    """
    return {
        "required": required,
        "values": values,
        "options": options
    }


def call_with_options(function, args, options):
    """
    Call a function with positional and keyword arguments.
    """
    return function(*args, **options)
