def word_frequencies(text: str) -> dict:
    """Count how many times each word occurs."""
    frequencies = {}

    for word in text.split():
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def safe_lookup(d: dict, key, default):
    """Return a value or a default without modifying the dictionary."""
    return d.get(key, default)


def increment(d: dict, key, amount: int) -> None:
    """Increment a dictionary value in place."""
    d[key] = d.get(key, 0) + amount


def dict_from_two_lists(keys: list, values: list) -> dict:
    """Build a dictionary using corresponding list positions."""
    result = {}

    for i in range(len(keys)):
        result[keys[i]] = values[i]

    return result


def merge_prefer_second(a: dict, b: dict) -> dict:
    """Merge dictionaries, preferring values from b."""
    result = dict(a)
    result.update(b)

    return result


def merge_counts(a: dict, b: dict) -> dict:
    """Merge two dictionaries by adding their counts."""
    result = dict(a)

    for key, value in b.items():
        result[key] = result.get(key, 0) + value

    return result


def group_by_first_letter(words: list) -> dict:
    """Group words by their lowercase first letter."""
    result = {}

    for word in words:
        if not word:
            continue

        key = word[0].lower()
        result.setdefault(key, []).append(word)

    return result


def add_defaults(config: dict, defaults: dict) -> None:
    """Insert missing configuration values in place."""
    for key, value in defaults.items():
        config.setdefault(key, value)


def remove_keys(d: dict, keys: list) -> int:
    """Remove specified keys and return the number removed."""
    removed = 0

    for key in keys:
        if key in d:
            del d[key]
            removed += 1

    return removed


def take_last(d: dict):
    """Remove and return the most recently inserted entry."""
    if not d:
        return None

    return d.popitem()


def remove_and_return(d: dict, key, default):
    """Remove a key and return its value or a default."""
    return d.pop(key, default)


def clear_and_report(d: dict) -> int:
    """Clear a dictionary and return its previous size."""
    previous_count = len(d)
    d.clear()

    return previous_count
