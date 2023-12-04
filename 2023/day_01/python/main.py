from part1 import Part1
from part2 import Part2

if __name__ == '__main__':
    part1 = Part1("C:/dev/adventofcode/2023/day_01/input.txt")

    part1_solution = part1.solve()

    print("Part 1: {}".format(part1_solution))

    part2 = Part2("C:/dev/adventofcode/2023/day_01/input.txt")

    print("Part 2: {}".format(part2.solve()))
