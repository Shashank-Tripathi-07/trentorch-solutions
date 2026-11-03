def append_all(lst: list, items: list) -> None:
    """
    Add every element of items to lst in place.
    """
    lst.extend(items)


def insert_sorted(lst: list, value) -> None:
    """
    Insert value after existing equal elements.
    """
    i = 0

    while i < len(lst) and lst[i] <= value:
        i += 1

    lst.insert(i, value)


def flatten_one_level(list_of_lists: list) -> list:
    """
    Flatten a list by one level without modifying the original.
    """
    result = []

    for inner_list in list_of_lists:
        result.extend(inner_list)

    return result


def concat_identity_report(lst: list, extra: list) -> list:
    """
    Compare list identity after += and +.
    """
    original_id = id(lst)

    lst += extra

    same_after_iadd = id(lst) == original_id

    original_id = id(lst)

    lst = lst + extra

    same_after_plus = id(lst) == original_id

    return [same_after_iadd, same_after_plus]


def remove_all(lst: list, value) -> None:
    """
    Remove every occurrence of value in place.
    """
    while value in lst:
        lst.remove(value)


def pop_last_n(lst: list, n: int) -> list:
    """
    Remove the last n elements and return them in original order.
    """
    if n <= 0:
        return []

    removed = lst[-n:]

    del lst[-n:]

    return removed


def delete_every_other(lst: list) -> None:
    """
    Delete elements at positions 0, 2, 4, ... in place.
    """
    del lst[::2]


def remove_first_or_report(lst: list, value) -> bool:
    """
    Remove the first occurrence if present.
    """
    if value in lst:
        lst.remove(value)
        return True

    return False
