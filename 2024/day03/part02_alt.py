import re
from functools import reduce


def read_instructions(file_path: str) -> list[tuple[int, str]]:
    with open(file_path, 'r') as f:
        _input = f.read()

        _pattern = "(?<=mul\()(\d+),(\d+)(?=\))|(do\(\))|(don\'t\(\))"

        _matches = [(match.start(), match.group()) for match in re.finditer(_pattern, _input)]

        return _matches

def do_calculation(instruction) -> int:
    return reduce(lambda x, y: x * y, [int(x) for x in instruction.split(",")])

def execute_instructions(execution_instructions):
    _accumulator = 0
    execute = True

    for instruction in execution_instructions:
        if instruction[1] == "do()":
            execute = True
        elif instruction[1] == "don't()":
            execute = False
        else:
            if execute:
                _accumulator += do_calculation(instruction[1])

    return _accumulator


instructions = read_instructions('input/actual.txt')

result = execute_instructions(instructions)

print(result)