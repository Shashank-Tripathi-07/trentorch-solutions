def receipt_line(item: str, qty: int, price: float) -> str:
    """
    Format item, quantity and price into aligned fields.
    """
    return f"{item:<12}{qty:>4}{price:>10.2f}"


def format_percent(value: float, decimals: int) -> str:
    """
    Convert a fraction into a formatted percentage.
    """
    return f"{value:.{decimals}%}"


def format_binary(n: int, width: int) -> str:
    """
    Convert n to binary with zero-padding.
    """
    return f"{n:0{width}b}"


def debug_label(label: str, value) -> str:
    """
    Format a label and the repr() of its value.
    """
    return f"{label}={value!r}"
