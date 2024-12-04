from day04methods import search_rows, search_columns, search_forward_diagonal, search_backwards_diagonal


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.read().split('\n')


crossword = read_input('input/actual.txt')

total = 0

total += search_rows(crossword, "XMAS")
total += search_rows(crossword, "SAMX")

total += search_columns(crossword, "XMAS")
total += search_columns(crossword, "SAMX")

total += search_forward_diagonal(crossword, "XMAS")
total += search_forward_diagonal(crossword, "SAMX")

total += search_backwards_diagonal(crossword, "XMAS")
total += search_backwards_diagonal(crossword, "SAMX")

print(total)