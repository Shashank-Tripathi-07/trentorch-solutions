def analyze_events(batches: list) -> tuple:
    """
    Analyze event IDs across multiple batches.
    """

    # Handle empty input
    if not batches:
        return ([], set(), set(), 0)

    # Step 1: Build unique IDs while preserving first-seen order
    unique_ids = []
    seen = set()

    for batch in batches:
        for event_id in batch:
            if event_id not in seen:
                seen.add(event_id)
                unique_ids.append(event_id)

    # Step 2: Convert each batch into a set
    batch_sets = [set(batch) for batch in batches]

    # Step 3: Find IDs common to every batch
    common_ids = batch_sets[0].copy()

    for batch_set in batch_sets[1:]:
        common_ids.intersection_update(batch_set)

    # Step 4: Construct the set of all IDs using a set comprehension
    all_ids = {event_id for batch_set in batch_sets for event_id in batch_set}

    # Step 5: Find IDs that are not common to every batch
    non_common_ids = all_ids - common_ids

    # Step 6: Count distinct IDs
    unique_count = len(all_ids)

    return (
        unique_ids,
        common_ids,
        non_common_ids,
        unique_count
    )
