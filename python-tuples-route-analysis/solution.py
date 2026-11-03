def analyze_route(points: list) -> tuple:
    """
    Analyze a route of (x, y) points.
    """

    # Handle an empty route
    if not points:
        return ({}, None, 0, 0, 0)

    # 1. Count visits using coordinate tuples as dictionary keys
    visit_counts = {}

    for point in points:
        if point in visit_counts:
            visit_counts[point] += 1
        else:
            visit_counts[point] = 1

    # 2. Calculate bounding box using comparisons
    first_x, first_y = points[0]

    min_x = max_x = first_x
    min_y = max_y = first_y

    for x, y in points:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    bounding_box = (
        (min_x, min_y),
        (max_x, max_y)
    )

    # 3. Calculate path length using an index loop
    path_length = 0

    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]

        path_length += abs(x2 - x1) + abs(y2 - y1)

    # 4. Calculate net displacement using extended unpacking
    if len(points) == 1:
        net_displacement = 0
    else:
        first, *_, last = points

        x1, y1 = first
        x2, y2 = last

        net_displacement = abs(x2 - x1) + abs(y2 - y1)

    # 5. Calculate revisit count
    revisit_count = len(points) - len(visit_counts)

    return (
        visit_counts,
        bounding_box,
        path_length,
        net_displacement,
        revisit_count
    )
