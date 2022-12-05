from dataclasses import dataclass
from collections import deque


@dataclass
class Instruction:
    move: int
    source: int
    target: int


def extract_crates(x):
    raw_crates = x.split('\n')
    num_stacks = int(x[-1])
    stack_list = []
    stack_indices = []
    index_stack_map = {
        1: 0,
        5: 1,
        9: 2,
        13: 3,
        17: 4,
        21: 5,
        25: 6,
        29: 7,
        33: 8
    }

    for ns in range(num_stacks):
        stack_list.append(deque([]))

    i = 0
    for c in raw_crates[-2]:
        if c.isalpha():
            stack_indices.append(i)
        i += 1

    for rc in raw_crates[:-1]:
        i = 0
        for c in rc:

            if i in index_stack_map.keys():
                if c != ' ':
                    stack_list[index_stack_map[i]].appendleft(c)
            i += 1

    return stack_list


def extract_instructions(x):
    raw_instructions = x.split('\n')
    instructions = []
    for i in raw_instructions:
        instruction = i.split(' ')
        instructions.append(Instruction(int(instruction[1]), int(instruction[3]), int(instruction[5])))

    return instructions


def parse_input(x):
    with open(x, 'r') as f:
        crates, instructions = f.read().split('\n\n')

        return extract_crates(crates), extract_instructions(instructions)


def execute_instructions(crates, instructions):
    print(crates)
    for instruction in instructions:
        for i in range(instruction.move):
            crates[instruction.target-1].append(crates[instruction.source-1].pop())

    top = []
    for crate in crates:
        top.append(crate.pop())

    print(''.join(top))


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle_input.txt'

    crates, instructions = parse_input(puzzle_input)

    execute_instructions(crates, instructions)


