from queue import PriorityQueue


class Coordinate(object):
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f'x: {self.x} y: {self.y}'

    def as_tuple(self):
        return (self.x, self.y)


class Sensor(object):
    def __init__(self, location, closest_beacon):
        self.location = location
        self.closest_beacon = closest_beacon

    def __repr__(self):
        return f'Sensor at x={self.location.x}, y={self.location.y}: closest beacon is at x={self.closest_beacon.x}, y={self.closest_beacon.y}'


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_input(x):
    raw_input = [
        sensor.split(':') for sensor in open(x).read()
            .replace('Sensor at ', '')
            .replace(' closest beacon is at ', '')
            .replace('x=', '')
            .replace(' y=', '')
            .split('\n')
    ]

    readout = []
    for sb in raw_input:
        s = sb[0].split(',')
        b = sb[1].split(',')
        readout.append(Sensor(Coordinate(s[0], s[1]), Coordinate(b[0], b[1])))

    return readout


def a_star_sensor(graph, start, distance):
    open_list = PriorityQueue()
    closed_list = {start: None}

    sensor_coverage = set()
    neighbor_offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    position = None

    # put the start into the queue
    open_list.put((0, start))

    while not open_list.empty():
        # get top priority (lowest risk) node from queue and blacklist it on closed_list
        position = open_list.get()[1]

        # for each neighbor of your current position
        for offset in neighbor_offsets:
            new_position = (position[0] + offset[0], position[1] + offset[1])
            print(new_position, end='\r')
            # if the new position is on the map
            if 0 <= new_position[0] < graph[0] and 0 <= new_position[1] < graph[1]:
                # if the new position is not black listed or presents a lower risk
                if new_position not in closed_list and manhattan_distance(start, new_position) <= distance:
                    sensor_coverage.add(new_position)
                    priority = manhattan_distance(start, new_position)
                    open_list.put((priority, new_position))
                    closed_list[new_position] = position

    return sensor_coverage


def part_1(readout, target_row):
    target_row_coverage = set()
    beacons = set()
    for ro in readout:
        beacons.add(ro.closest_beacon.as_tuple())

        beacon_distance = manhattan_distance((ro.location.x, ro.location.y), (ro.closest_beacon.x, ro.closest_beacon.y))
        vertical_window = (ro.location.y + beacon_distance, ro.location.y - beacon_distance)

        # if the sensor and its closest beacon add coverage to the target row
        if vertical_window[0] >= target_row >= vertical_window[1]:
            # calculate the coverage at center for the sensor
            current_coverage = (beacon_distance * 2) + 1

            # calculate how far away the target_row is
            target_row_distance = abs(ro.location.y - target_row)

            # for that many times, subtract 2 from the current coverage
            current_coverage = current_coverage - (target_row_distance*2)

            # calculate the points of that coverage
            left_right = (current_coverage - 1) // 2
            for x in list(range(ro.location.x - left_right, ro.location.x + left_right + 1)):
                target_row_coverage.add((x, target_row))

    coverage = len(target_row_coverage)
    beacons = len([b for b in beacons if b[1] == target_row])

    return coverage - beacons


def collapse_coverage(sorted_row_coverage, debug=False):
    if debug:
        print(f'Input: {sorted_row_coverage}')
    if len(sorted_row_coverage) == 1:
        return sorted_row_coverage
    if len(sorted_row_coverage) == 2 and sorted_row_coverage[0][1] < sorted_row_coverage[1][0]:
        return sorted_row_coverage
    else:
        # remove fully contained ranges
        to_remove = set()
        for rng in sorted_row_coverage:
            if any(rng[0] >= src[0] and rng[1] <= src[1] and rng != src for src in sorted_row_coverage):
                if debug:
                    print(f'Removing {rng} from {sorted_row_coverage}')
                    input()
                to_remove.add(rng)

        for tr in to_remove:
            sorted_row_coverage.remove(tr)

        # if there's only one left after let's return
        if len(sorted_row_coverage) == 1:
            return sorted_row_coverage

        pairs = list(zip(sorted_row_coverage, sorted_row_coverage[1:]))
        if debug:
            print(f'Pairs: {pairs}')
            input()
        new_sorted_row_coverage = []

        for pair in pairs:
            if pair[0][1] >= pair[1][0]:
                right_most = max(pair[0][1], pair[1][1])
                new_sorted_row_coverage.append((pair[0][0], right_most))
            else:
                new_sorted_row_coverage.append(pair[0])
                new_sorted_row_coverage.append(pair[1])

        next_iteration = sorted(list(set(new_sorted_row_coverage)), key=lambda x: x[0])
        if debug:
            print(f'Input  : {sorted_row_coverage}')
            print(f'Passing: {next_iteration}')
            input()
        return collapse_coverage(next_iteration, debug)


def part_2(readout, cave_size):
    row_with_hole = 0
    for target_row in range(0, cave_size):
        beacons = set()
        row_coverage = []
        for ro in readout:
            beacons.add(ro.closest_beacon.as_tuple())

            beacon_distance = manhattan_distance((ro.location.x, ro.location.y), (ro.closest_beacon.x, ro.closest_beacon.y))
            y_min = 0 if ro.location.y - beacon_distance < 0 else ro.location.y - beacon_distance
            y_max = cave_size if ro.location.y + beacon_distance > cave_size else ro.location.y + beacon_distance
            vertical_window = (y_max, y_min)

            # if the sensor and its closest beacon add coverage to the target row
            if vertical_window[0] >= target_row >= vertical_window[1]:
                # calculate the coverage at center for the sensor
                current_coverage = (beacon_distance * 2) + 1

                # calculate how far away the target_row is
                target_row_distance = abs(ro.location.y - target_row)

                # for that many times, subtract 2 from the current coverage
                current_coverage = current_coverage - (target_row_distance * 2)

                # calculate the points of that coverage within the confines of the cave
                left_right = (current_coverage - 1) // 2
                x_min = 0 if ro.location.x - left_right < 0 else ro.location.x - left_right
                x_max = cave_size if ro.location.x + left_right > cave_size else ro.location.x + left_right
                row_coverage.append((x_min, x_max))

        collapsed_row_coverage = collapse_coverage(sorted(row_coverage, key=lambda x: x[0]))
        if collapsed_row_coverage != [(0, cave_size)]:
            row_with_hole = target_row
            break

    exposed_nodes = set()
    for x in range(0, cave_size + 1):
        exposed_nodes.add((x, row_with_hole))
    for ro in readout:
        beacon_distance = manhattan_distance((ro.location.x, ro.location.y), (ro.closest_beacon.x, ro.closest_beacon.y))
        vertical_window = (ro.location.y + beacon_distance, ro.location.y - beacon_distance)

        # if the sensor and its closest beacon add coverage to the target row
        if vertical_window[0] >= target_row >= vertical_window[1]:
            # calculate the coverage at center for the sensor
            current_coverage = (beacon_distance * 2) + 1

            # calculate how far away the target_row is
            target_row_distance = abs(ro.location.y - target_row)

            # for that many times, subtract 2 from the current coverage
            current_coverage = current_coverage - (target_row_distance * 2)

            # calculate the points of that coverage
            left_right = (current_coverage - 1) // 2
            x_min = 0 if ro.location.x - left_right < 0 else ro.location.x - left_right
            x_max = cave_size if ro.location.x + left_right > cave_size else ro.location.x + left_right
            for x in list(range(x_min, x_max + 1)):
                try:
                    exposed_nodes.remove((x, target_row))
                except KeyError:
                    pass

    exposed_node = exposed_nodes.pop()

    return exposed_node[0] * 4000000 + exposed_node[1]


if __name__ == '__main__':
    simple_input = './input/simple.txt'
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    readout = parse_input(puzzle_input)

    coverage = part_1(readout, 2000000)

    print(f'Part 1: {coverage}')

    tuning_frequency = part_2(readout, 4000000)

    print(f'Part 2: {tuning_frequency}')
