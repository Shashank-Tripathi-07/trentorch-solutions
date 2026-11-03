def edge_key(a: int, b: int) -> tuple:
    """
    Return a canonical key for an undirected edge.
    """
    return (min(a, b), max(a, b))


def count_visits(path: list) -> dict:
    """
    Count occurrences of each distinct coordinate tuple.
    """
    counts = {}

    for point in path:
        if point in counts:
            counts[point] += 1
        else:
            counts[point] = 1

    return counts


def group_points_by_cell(points: list, cell_size: int) -> dict:
    """
    Group points by their grid cell.
    """
    groups = {}

    for x, y in points:
        cell = (x // cell_size, y // cell_size)

        if cell in groups:
            groups[cell].append((x, y))
        else:
            groups[cell] = [(x, y)]

    return groups
