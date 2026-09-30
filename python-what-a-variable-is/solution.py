def compute_total(price: float, quantity: int) -> float:
    subtotal = price * quantity
    tax = subtotal * 0.08
    subtotal += tax
    return subtotal


def swap_two_variables(a, b):
    temp = a      # pour cup A into the spare cup
    a = b         # pour cup B into cup A
    b = temp      # pour the spare cup into cup B
    return a, b
