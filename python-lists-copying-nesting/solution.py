import copy


def shallow_copy(lst: list) -> list:
    """
    Return a new list with the same elements.
    """
    return lst.copy()


def deep_copy(nested: list) -> list:
    """
    Return a fully independent copy of a nested structure.
    """
    return copy.deepcopy(nested)


def shares_inner_objects(original: list, duplicate: list) -> bool:
    """
    Check whether corresponding elements are identical objects.
    """
    if len(original) != len(duplicate):
        return False

    for a, b in zip(original, duplicate):
        if a is not b:
            return False

    return True


def add_row_safely(matrix: list, row: list) -> list:
    """
    Return a new matrix with independent copies of every row.
    """
    result = [copy.deepcopy(existing_row) for existing_row in matrix]

    result.append(copy.deepcopy(row))

    return result


def make_grid(rows: int, cols: int, fill) -> list:
    """
    Create a grid with independent row objects.
    """
    return [[copy.deepcopy(fill) for _ in range(cols)] for _ in range(rows)]


def rows_are_independent(grid: list) -> bool:
    """
    Check whether every row has a unique identity.
    """
    seen_ids = set()

    for row in grid:
        row_id = id(row)

        if row_id in seen_ids:
            return False

        seen_ids.add(row_id)

    return True


def transpose(matrix: list) -> list:
    """
    Swap rows and columns without modifying the original.
    """
    return [
        [matrix[row][col] for row in range(len(matrix))]
        for col in range(len(matrix[0]))
    ]
