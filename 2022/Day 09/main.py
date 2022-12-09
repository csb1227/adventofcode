def open_ropes(r):
    with open(r, 'r') as f:
        return f.read().split('\n')


class Instruction(object):
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = int(distance)
        self.step_dict = {
            'U': Coordinate(0, 1),
            'D': Coordinate(0, -1),
            'R': Coordinate(1, 0),
            'L': Coordinate(-1, 0),
            'UR': Coordinate(1, 1),
            'UL': Coordinate(-1, 1),
            'DR': Coordinate(1, -1),
            'DL': Coordinate(-1, -1)
        }

    def __repr__(self):
        return (self.direction, self.distance)

    def __str__(self):
        return f'{self.direction} {self.distance}'

    def steps(self):
        for s in range(self.distance):
            yield self.step_dict[self.direction]


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def shift(self, coordinate):
        self.x += coordinate.x
        self.y += coordinate.y


class Knot(object):
    def __init__(self, coordinate, order=0, followed_by=None):
        self.coordinate = coordinate
        self.order = order
        self.path = [str(Coordinate(0, 0))]
        self.followed_by = followed_by

    def __str__(self):
        return f'Knot {self.order}.\n' \
               f'Coordinate: {self.coordinate}\n' \
               f'Path: {self.path}\n' \
               f'Visited: {self.get_visited()}'

    def get_visited(self):
        return len(set(self.path))

    def move(self, instruction):
        for step in instruction.steps():
            self.coordinate.shift(step)
            self.path.append(str(Coordinate(self.coordinate.x, self.coordinate.y)))
            if self.followed_by:
                x_diff = self.coordinate.x - self.followed_by.coordinate.x
                y_diff = self.coordinate.y - self.followed_by.coordinate.y

                if x_diff > 1 and y_diff == 0:
                    self.followed_by.move(Instruction('R', 1))
                elif x_diff < -1 and y_diff == 0:
                    self.followed_by.move(Instruction('L', 1))
                elif x_diff == 0 and y_diff > 1:
                    self.followed_by.move(Instruction('U', 1))
                elif x_diff == 0 and y_diff < -1:
                    self.followed_by.move(Instruction('D', 1))

                elif (x_diff >= 1 and y_diff > 1) or (x_diff > 1 and y_diff >= 1):
                    self.followed_by.move(Instruction('UR', 1))
                elif (x_diff <= -1 and y_diff > 1) or (x_diff < -1 and y_diff >= 1):
                    self.followed_by.move(Instruction('UL', 1))
                elif (x_diff >= 1 and y_diff < -1) or (x_diff > 1 and y_diff <= -1):
                    self.followed_by.move(Instruction('DR', 1))
                elif (x_diff <= -1 and y_diff < -1) or (x_diff < -1 and y_diff <= -1):
                    self.followed_by.move(Instruction('DL', 1))


class Rope(object):
    def __init__(self, num_knots, starting_coordinate):
        self.starting_coordinate = starting_coordinate
        self.knots = self.tie_rope(num_knots)

    def tie_rope(self, num_knots):
        r = []
        for nk in range(num_knots):
            r.append(Knot(Coordinate(self.starting_coordinate.x, self.starting_coordinate.y)))

        for ix, k in enumerate(r):
            k.order = ix
            if ix < len(r)-1:
                k.followed_by = r[ix + 1]

        return r


def execute_instructions(rope, instructions):
    for instruction in instructions:
        rope.knots[0].move(instruction)


if __name__ == '__main__':
    example_input = './input/example.txt'
    example_input2 = './input/example_part2.txt'
    puzzle_input = './input/puzzle_input.txt'
    part1_example = [Instruction(i[0], i[1]) for i in [instruction.split(' ') for instruction in open_ropes(example_input)]]
    part2_example = [Instruction(i[0], i[1]) for i in [instruction.split(' ') for instruction in open_ropes(example_input2)]]
    instructions = [Instruction(i[0], i[1]) for i in [instruction.split(' ') for instruction in open_ropes(puzzle_input)]]

    rope1 = Rope(2, Coordinate(0, 0))
    rope2 = Rope(10, Coordinate(11, 5))

    execute_instructions(rope1, instructions)
    execute_instructions(rope2, instructions)

    print(f'Part 1: {rope1.knots[-1].get_visited()}')
    print(f'Part 2: {rope2.knots[-1].get_visited()}')
