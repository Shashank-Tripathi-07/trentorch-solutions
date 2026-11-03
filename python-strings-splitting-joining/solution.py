def word_count(text: str) -> int:
    """
    Count words separated by whitespace.
    """
    return len(text.split())


def reverse_word_order(text: str) -> str:
    """
    Reverse word order and join with single spaces.
    """
    return " ".join(text.split()[::-1])


def last_field(line: str, sep: str) -> str:
    """
    Return the text after the last occurrence of sep.
    """
    return line.rsplit(sep, 1)[-1]


def count_nonblank_lines(text: str) -> int:
    """
    Count lines containing at least one non-whitespace character.
    """
    count = 0

    for line in text.splitlines():
        if line.strip():
            count += 1

    return count


def make_csv_line(fields) -> str:
    """
    Join fields with commas, quoting fields containing commas.
    """
    formatted_fields = []

    for field in fields:
        if "," in field:
            field = '"' + field + '"'

        formatted_fields.append(field)

    return ",".join(formatted_fields)
