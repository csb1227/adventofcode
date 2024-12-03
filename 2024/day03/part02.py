import re
from functools import reduce


def read_instructions(file_path: str) -> tuple[
    list[tuple[int, list[int]]], list[tuple[int, str]], list[tuple[int, str]]]:
    with open(file_path, 'r') as f:
        _input = f.read()

        _mul_pattern = "(?<=mul\()(\d+),(\d+)(?=\))"
        _mul_matches = [(match.start(), [int(x) for x in match.group().split(',')]) for match in re.finditer(_mul_pattern, _input)]

        _do_pattern = "do\(\)"
        _do_matches = [(match.start(), "True") for match in re.finditer(_do_pattern, _input)]

        _dont_pattern = "don\'t\(\)"
        _dont_matches = [(match.start(), "False") for match in re.finditer(_dont_pattern, _input)]

        return _mul_matches, _do_matches, _dont_matches


def do_calculation(instruction: list) -> int:
    return reduce(lambda x, y: x * y, instruction)

def reduce_instructions(multiply_instructions, do_instructions, dont_instructions):
    _mul_calculated = [(x, do_calculation(y)) for x, y in multiply_instructions]
    return sorted(do_instructions + dont_instructions + _mul_calculated, key=lambda x: x[0])

def execute_instructions(instructions):
    _accumulator = 0
    execute = True

    for instruction in instructions:
        if instruction[1] == "True":
            execute = True
        elif instruction[1] == "False":
            execute = False
        else:
            if execute:
                _accumulator += instruction[1]

    return _accumulator


mul, do, dont = read_instructions('input/actual.txt')

_reduced_instructions = reduce_instructions(mul, do, dont)

print(execute_instructions(_reduced_instructions))
