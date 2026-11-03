def compare_strings(a: str, b: str) -> int:
    """
    Compare strings lexicographically using character code points.
    """
    min_length = min(len(a), len(b))

    for i in range(min_length):
        code_a = ord(a[i])
        code_b = ord(b[i])

        if code_a < code_b:
            return -1
        elif code_a > code_b:
            return 1

    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1

    return 0


def compare_ignoring_case(a: str, b: str) -> int:
    """
    Compare strings after case folding.
    """
    a = a.casefold()
    b = b.casefold()

    if a < b:
        return -1
    elif a > b:
        return 1

    return 0


def caesar_shift(s: str, k: int) -> str:
    """
    Shift ASCII letters while preserving their case.
    """
    result = []

    for char in s:
        if 'a' <= char <= 'z':
            shifted = (ord(char) - ord('a') + k) % 26
            result.append(chr(ord('a') + shifted))

        elif 'A' <= char <= 'Z':
            shifted = (ord(char) - ord('A') + k) % 26
            result.append(chr(ord('A') + shifted))

        else:
            result.append(char)

    return "".join(result)


def utf8_byte_length(s: str) -> int:
    """
    Return the number of UTF-8 encoded bytes.
    """
    return len(s.encode("utf-8"))


def roundtrip(s: str, encoding: str) -> str:
    """
    Encode and decode using the specified encoding.
    """
    encoded = s.encode(encoding, errors="replace")
    return encoded.decode(encoding)


def is_ascii_only(s: str) -> bool:
    """
    Check whether all characters are ASCII using byte length.
    """
    return len(s) == len(s.encode("utf-8"))


def first_byte_values(s: str, count: int) -> list:
    """
    Return integer values of the first count UTF-8 bytes.
    """
    return list(s.encode("utf-8")[:count])
