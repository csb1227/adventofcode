def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return f.read().split('\n')


def make_turn(turn: str) -> int:
    number = int(turn[1:])
    if turn[0] == 'L':
        number *= -1

    return number