import copy


def label_of(row: list) -> str:
    """
    Return the label of an inventory row.
    """
    return row[0]


def quantity_of(row: list) -> int:
    """
    Return the quantity of an inventory row.
    """
    return row[1]


def process_inventory(rows: list, min_qty: int) -> list:
    """
    Filter, sort and summarize inventory rows in place.
    """

    # Step 1: Take an independent snapshot
    snapshot = copy.deepcopy(rows)

    # Step 2: Remove rows below minimum quantity in place
    rows[:] = [row for row in rows if quantity_of(row) >= min_qty]

    # Step 3: Stable sorting (least important key first)

    # First sort by label in ascending order
    rows.sort(key=label_of)

    # Then sort by quantity in descending order
    # Stability preserves label order when quantities are equal
    rows.sort(key=quantity_of, reverse=True)

    # Step 4: Get labels of the first three rows
    top_labels = [label_of(row) for row in rows[:3]]

    # Step 5: Get quantities of all remaining rows
    quantities = [quantity_of(row) for row in rows]

    return [snapshot, top_labels, quantities]
