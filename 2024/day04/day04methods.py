import re


def search_rows(crossword: list[str], pattern: str) -> int:
    _pattern_occurrences = 0
    for row in crossword:
        _pattern_occurrences += row.count(pattern)

    return _pattern_occurrences

def search_columns(crossword: list[str], pattern: str) -> int:
    _pattern_occurrences = 0

    _crossword_columns = []

    for i in range(len(crossword[0])):
        _crossword_columns.append(''.join([row[i] for row in crossword]))

    _pattern_occurrences = search_rows(_crossword_columns, pattern)

    return _pattern_occurrences

def search_forward_diagonal(crossword: list[str], pattern: str) -> int:
    _pattern_occurrences = 0

    _crossword_diagonal = []

    _width = len(crossword[0])
    _height = len(crossword)

    # top row
    for x in range(_width - len(pattern) + 1):
        y = 0
        _this_diagonal = []
        while y < _height and x < _width:
            _this_diagonal.append(crossword[y][x])
            x += 1
            y += 1

        _crossword_diagonal.append("".join(_this_diagonal))

    # left column
    for y in range(1, _height - len(pattern) + 1):
        x = 0
        _this_diagonal = []
        while y < _height and x < _width:
            _this_diagonal.append(crossword[y][x])
            x += 1
            y += 1

        _crossword_diagonal.append("".join(_this_diagonal))

    _pattern_occurrences += search_rows(_crossword_diagonal, pattern)

    return _pattern_occurrences

def search_backwards_diagonal(crossword: list[str], pattern: str) -> int:
    _mirrored_crossword = [row[::-1] for row in crossword]

    _pattern_occurrences = search_forward_diagonal(_mirrored_crossword, pattern)

    return _pattern_occurrences


def create_groups(crossword: list[str], group_size: int) -> (list[list[str]], int):
    _row_groups = []

    for i in range(len(crossword) - (group_size - 1)):
        _row_groups.append("".join(crossword[i:i + group_size]))

    return _row_groups, len(crossword[0])

def count_x_mas(row_groups: list[str], row_length: int) -> int:
    _top_m_pattern = f"(?=(M[A-Z]M[A-Z]{{{row_length - 2}}}A[A-Z]{{{row_length - 2}}}S[A-Z]S))"
    _right_m_pattern = f"(?=(S[A-Z]M[A-Z]{{{row_length - 2}}}A[A-Z]{{{row_length - 2}}}S[A-Z]M))"
    _bottom_m_pattern = f"(?=(S[A-Z]S[A-Z]{{{row_length - 2}}}A[A-Z]{{{row_length - 2}}}M[A-Z]M))"
    _left_m_pattern = f"(?=(M[A-Z]S[A-Z]{{{row_length - 2}}}A[A-Z]{{{row_length - 2}}}M[A-Z]S))"

    _matches = []

    for group in row_groups:
        _matches.append(re.findall(_top_m_pattern, group))
        _matches.append(re.findall(_right_m_pattern, group))
        _matches.append(re.findall(_bottom_m_pattern, group))
        _matches.append(re.findall(_left_m_pattern, group))

    return sum(len(match) for match in _matches)


