import re
from functools import reduce


def read_instructions(file_path: str) -> list:
    with open(file_path, 'r') as f:
        _pattern = "(?<=mul\()(\d+),(\d+)(?=\))"
        _matches = re.findall(_pattern, f.read())

        return [[int(x) for x in match] for match in _matches]


def do_calculation(instruction: list) -> int:
    return reduce(lambda x, y: x * y, instruction)


instructions = read_instructions('input/actual.txt')

print(sum([do_calculation(instruction) for instruction in instructions]))
