def open_ropes(r):
    with open(r, 'r') as f:
        return f.read().split('\n')


class Instruction(object):
    def __init__(self, raw_instruction):
        self.direction = raw_instruction[0]
        self.distance = int(raw_instruction[1])

    def __repr__(self):
        return f'{self.direction} {self.distance}'


class Knot(object):
    def __init__(self, name):
        self.name = name
        self.coords = (0, 0)
        self.path = [(0, 0)]

    def __repr__(self):
        return f'{self.name} knot\n' \
               f'{self.coords}\n' \
               f'{self.path}\n' \
               f'visited: {len(set(self.visited))}\n'

    def get_visited_coords(self):
        return set(self.path)

    visited = property(get_visited_coords, None)

    def move(self, instruction, tail=None):
        if instruction.direction == 'U':
            for y in range(instruction.distance):
                next_coords = (self.coords[0], self.coords[1] + y + 1)
                self.path.append(next_coords)
                if tail:
                    tail.follow(self.path)
            self.coords = self.path[-1]

        elif instruction.direction == 'R':
            for x in range(instruction.distance):
                next_coords = (self.coords[0] + x + 1, self.coords[1])
                self.path.append(next_coords)
                if tail:
                    tail.follow(self.path)
            self.coords = self.path[-1]

        elif instruction.direction == 'D':
            for y in range(instruction.distance):
                next_coords = (self.coords[0], self.coords[1] - y - 1)
                self.path.append(next_coords)
                if tail:
                    tail.follow(self.path)
            self.coords = self.path[-1]

        else:
            for x in range(instruction.distance):
                next_coords = (self.coords[0] - x - 1, self.coords[1])
                self.path.append(next_coords)
                if tail:
                    tail.follow(self.path)
            self.coords = self.path[-1]

    def follow(self, leader_path):
        x_diff = leader_path[-1][0] - self.coords[0]
        y_diff = leader_path[-1][1] - self.coords[1]

        if x_diff > 1:
            self.coords = (leader_path[-1][0]-1, leader_path[-1][1])
        if x_diff < -1:
            self.coords = (leader_path[-1][0] + 1, leader_path[-1][1])
        if y_diff > 1:
            self.coords = (leader_path[-1][0], leader_path[-1][1] - 1)
        if y_diff < -1:
            self.coords = (leader_path[-1][0], leader_path[-1][1] + 1)

        self.path.append(self.coords)


def execute_instructions(instructions):
    head = Knot('head')
    tail = Knot('tail')

    for instruction in instructions:
        head.move(instruction, tail)

    return head, tail


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle_input.txt'
    instructions = [Instruction(instruction.split(' ')) for instruction in open_ropes(puzzle_input)]
    # print(instructions)
    head, tail = execute_instructions(instructions)

    print(f'Part 1: {len(tail.visited)}')
