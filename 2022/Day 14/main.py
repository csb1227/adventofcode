import copy
import logging


class Coordinate(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f'x: {self.x} y: {self.y}'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def x_offset(self, offset):
        return self.x - offset


class RockLine(object):
    def __init__(self, ends):
        self.a = ends[0]
        self.b = ends[1]

    def get_line(self):
        if self.a == self.b:
            print('Just a lone rock')
            input()
        elif self.a.x == self.b.x:
            return self.vertical_line()
        elif self.a.y == self.b.y:
            return self.horizontal_line()

    def horizontal_line(self):
        if self.a.x > self.b.x:
            return [Coordinate(x, self.a.y) for x in range(self.b.x, self.a.x + 1)]
        else:
            return [Coordinate(x, self.a.y) for x in range(self.a.x, self.b.x + 1)]

    def vertical_line(self):
        if self.a.y > self.b.y:
            return [Coordinate(self.a.x, y) for y in range(self.b.y, self.a.y + 1)]
        else:
            return [Coordinate(self.a.x, y) for y in range(self.a.y, self.b.y + 1)]


def parse_input(x):
    raw_input = [path for path in open(x).read().split('\n')]

    rock_paths = [path.split(' -> ') for path in raw_input]

    rock_line_end_coordinates = []
    for rock_path in rock_paths:
        raw_coordinates = [xy.split(',') for xy in rock_path]
        coordinates = [Coordinate(xy[0], xy[1]) for xy in raw_coordinates]
        rock_line_end_coordinates.append(list(zip(coordinates, coordinates[1:])))

    rock_locations = []
    for rock_line_end_coordinate in rock_line_end_coordinates:
        for rocks in rock_line_end_coordinate:
            rock_locations.extend(RockLine(rocks).get_line())

    xmin, xmax = 500, 500
    ymin, ymax = 0, 0
    for rock in rock_locations:
        xmin = rock.x if rock.x < xmin else xmin
        xmax = rock.x if rock.x > xmax else xmax
        ymin = rock.y if rock.y < ymin else ymin
        ymax = rock.y if rock.y > ymax else ymax

    row = '.' * (xmax - xmin + 1)
    cave = []
    for y in range(ymin, ymax + 1):
        cave.append([air for air in row])

    for rock_location in rock_locations:
        cave[rock_location.y][rock_location.x_offset(xmin)] = '#'

    sand_start = Coordinate(500 - xmin, 0)

    return cave, sand_start


def add_a_floor(cave, sand_start):
    # the base of this sand pyramid could end up being as wide as the height*2 - 1
    buffer = '.' * len(cave)

    expanded_cave = []
    for c in cave:
        expanded_cave.append([b for b in buffer] + c + [b for b in buffer])

    expanded_cave.append([b for b in '.' * len(expanded_cave[0])])
    expanded_cave.append([b for b in '#' * len(expanded_cave[0])])

    return expanded_cave, Coordinate(sand_start.x + len(cave), sand_start.y)


def falling_sand(cave, sand_start):
    try:
        settled = False
        position = copy.copy(sand_start)
        while not settled:
            # can i fall straight down
            if cave[position.y+1][position.x] == '.':
                position.y += 1
            # if not can i fall down-left
            elif cave[position.y+1][position.x-1] == '.':
                position.y += 1
                position.x -= 1
            # if not can i fall down-right
            elif cave[position.y+1][position.x+1] == '.':
                position.y += 1
                position.x += 1
            # sand at the start
            elif cave[position.y][position.x] == 'o':
                settled = True
                return cave, False
            # if not then i am settled
            else:
                cave[position.y][position.x] = 'o'
                settled = True
    except IndexError:
        return cave, False

    return cave, True


def simulation(cave, sand_start):
    filling = True
    units = 0
    while filling:
        cave, filling = falling_sand(cave, sand_start)
        units += 1 if filling else 0

    for c in cave:
        print(''.join(c))

    return units


if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR, format='%(message)s')

    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    cave, sand_start = parse_input(example_input)

    print(f'Part 1: {simulation(copy.copy(cave), copy.copy(sand_start))}')

    cave_2, sand_start_2 = parse_input(puzzle_input)
    cave_2, sand_start_2 = add_a_floor(cave_2, sand_start_2)

    print(f'Part 2: {simulation(copy.copy(cave_2), copy.copy(sand_start_2))}')

