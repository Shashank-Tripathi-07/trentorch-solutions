def sentence_case(s: str) -> str:
    """
    First character uppercase, remaining characters lowercase.
    """
    if not s:
        return ""

    return s[0].upper() + s[1:].lower()


def swap_first_char_case(s: str) -> str:
    """
    Swap the case of only the first character.
    """
    if not s:
        return ""

    return s[0].swapcase() + s[1:]


def equal_ignoring_case(a: str, b: str) -> bool:
    """
    Compare strings using Unicode-aware case folding.
    """
    return a.casefold() == b.casefold()


def case_kind(s: str) -> str:
    """
    Classify the case of a string.
    """
    if s.isupper():
        return "upper"
    elif s.islower():
        return "lower"
    elif s.istitle():
        return "title"
    else:
        return "mixed"


def find_all(s: str, sub: str) -> list:
    """
    Find all occurrences, including overlapping ones.
    """
    if sub == "":
        return []

    result = []
    start = 0

    while True:
        index = s.find(sub, start)

        if index == -1:
            break

        result.append(index)
        start = index + 1

    return result


def count_overlapping(s: str, sub: str) -> int:
    """
    Count overlapping occurrences.
    """
    return len(find_all(s, sub))


def has_extension(filename: str, ext: str) -> bool:
    """
    Check whether filename ends with .ext, ignoring case.
    """
    return filename.casefold().endswith("." + ext.casefold())


def classify_token(token: str) -> str:
    """
    Classify a token based on its characters.
    """
    if not token:
        return "other"

    elif token.isdigit():
        return "digits"

    elif token.isalpha():
        return "letters"

    elif token.isalnum():
        return "alnum"

    elif token.isspace():
        return "space"

    else:
        return "other"


def clean_field(s: str) -> str:
    """
    Remove surrounding whitespace and trailing punctuation.
    """
    return s.strip().rstrip(".,;").strip()


def remove_prefix_once(s: str, prefix: str) -> str:
    """
    Remove a prefix exactly once if present.
    """
    if s.startswith(prefix):
        return s[len(prefix):]

    return s


def replace_first_n(s: str, old: str, new: str, n: int) -> str:
    """
    Replace the first n occurrences of old with new.
    """
    if n == 0:
        return s

    return s.replace(old, new, n)
