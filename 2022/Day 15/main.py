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


def part_one(readout, target_row):
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


if __name__ == '__main__':
    simple_input = './input/simple.txt'
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    readout = parse_input(puzzle_input)

    coverage = part_one(readout, 2000000)

    print(f'Part 1: {coverage}')
