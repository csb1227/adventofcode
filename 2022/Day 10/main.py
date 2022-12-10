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


def execute_instructions(communicator, instructions):
    for instruction in instructions:
        if instruction.operation == 'noop':
            communicator.cpu.stack.append(0)
        elif instruction.operation == 'addx':
            communicator.cpu.stack.extend([0, instruction.value])

    communicator.cpu.stack = list(reversed(communicator.cpu.stack))

    while len(communicator.cpu.stack) > 0:
        communicator.cpu.cycle += 1

        if communicator.cpu.cycle in [20, 60, 100, 140, 180, 220]:
            communicator.signal_strength += (communicator.cpu.cycle * communicator.cpu.X)

        communicator.draw()

        communicator.cpu.X += communicator.cpu.stack.pop()


class Communicator(object):
    def __init__(self):
        self.cpu = CPU()
        self.display = Display()
        self.signal_strength = 0

    def __str__(self):
        return f'Cycle: {self.cpu.cycle}\n' \
               f'X:     {self.cpu.X}\n' \
               f'Sprite:{list(range(self.cpu.X - 1, self.cpu.X + 2))}\n' \
               f'{self.display}'

    def draw(self):
        if (self.cpu.cycle % 40) - 1 in list(range(self.cpu.X - 1, self.cpu.X + 2)):
            self.display.pixels.append('█')
        else:
            self.display.pixels.append(' ')


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
        self.pixels = []

    def __str__(self):
        return '\n'.join(self._wrap_lines())

    def _wrap_lines(self):
        for i in range(0, len(self.pixels), 40):
            yield ''.join(self.pixels[i:i + 40])


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

    communicator = Communicator()

    execute_instructions(communicator, instructions)

    print(f'Part 1: {communicator.signal_strength}')
    print('Part 2:')
    print(communicator.display)
