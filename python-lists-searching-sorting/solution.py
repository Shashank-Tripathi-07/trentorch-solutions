def index_or_minus_one(lst: list, value) -> int:
    """
    Return the first matching index, or -1 if not found.
    """
    if value in lst:
        return lst.index(value)

    return -1


def all_indices(lst: list, value) -> list:
    """
    Return all indices where elements equal value.
    """
    return [i for i, item in enumerate(lst) if item == value]


def contains_all(lst: list, needles: list) -> bool:
    """
    Check whether every element in needles exists in lst.
    """
    for item in needles:
        if item not in lst:
            return False

    return True


def contains_same_object(lst: list, target) -> bool:
    """
    Check whether target is the exact same object as an element.
    """
    for item in lst:
        if item is target:
            return True

    return False


def sorted_desc_copy(lst: list) -> list:
    """
    Return a new list sorted in descending order.
    """
    return sorted(lst, reverse=True)


def sort_in_place_by_length(words: list) -> None:
    """
    Sort words in place by length.
    """
    words.sort(key=len)


def last_char(word: str) -> str:
    """
    Return the last character, or an empty string.
    """
    if not word:
        return ""

    return word[-1]


def sort_by_last_char(words: list) -> list:
    """
    Return a new list sorted by the last character.
    """
    return sorted(words, key=last_char)


def reversed_copy(lst: list) -> list:
    """
    Return a new reversed list.
    """
    return list(reversed(lst))
