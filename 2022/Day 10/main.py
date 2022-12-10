from collections import defaultdict

def parse_raw_instructions(raw_instructions):
    instructions = []

    for ix, i in enumerate(raw_instructions):
        if i[0] == 'noop':
            instructions.append(Instruction('noop', 0, ix + 1))
        else:
            instructions.append(Instruction(i[0], i[1], ix + 1))

    return instructions


def open_instructions(r):
    with open(r, 'r') as f:
        return [i.split(' ') for i in f.read().split('\n')]


def execute_instructions(cpu, instructions):
    signal_strength = 0
    for instruction in instructions:
        if instruction.operation == 'noop':
            cpu.stack.append(0)
        elif instruction.operation == 'addx':
            cpu.stack.extend([0, instruction.value])

    cpu.stack = list(reversed(cpu.stack))

    while len(cpu.stack) > 0:
        cpu.cycle += 1
        if cpu.cycle in [20, 60, 100, 140, 180, 220]:
            signal_strength += (cpu.cycle * cpu.X)
            print(cpu)

        cpu.X += cpu.stack.pop()

    return signal_strength


class CPU(object):
    def __init__(self):
        self.cycle = 0
        self.X = 1
        self.stack = []

    def __repr__(self):
        return f'Cycles: {self.cycle}\n' \
               f'X: {self.X}\n'

class Display(object):
    def __init__(self):
        self.pixels = [['.'*40]*6]


class Instruction(object):
    def __init__(self, operation, value, cycle):
        self.operation = operation
        self.value = int(value) if value else 0
        self.cycle_start = cycle
        self.cycle_finish = cycle if operation == 'noop' else cycle + 2
        self.completed = False

    def __repr__(self):
        return f'{self.cycle_start} {self.operation} {self.value}'

    def __str__(self):
        return f'{self.cycle_start} {self.operation} {self.value}'


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    raw_instructions = open_instructions(puzzle_input)
    instructions = parse_raw_instructions(raw_instructions)
    cpu = CPU()

    signal_strength = execute_instructions(cpu, instructions)

    print(f'Part 1: {signal_strength}')

