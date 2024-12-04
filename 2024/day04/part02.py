from day04methods import create_groups, count_x_mas


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.read().split('\n')


crossword = read_input('input/actual.txt')

row_groups, row_length = create_groups(crossword, 3)

result = count_x_mas(row_groups, row_length)

print(result)