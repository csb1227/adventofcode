from cube_game import CubeGame

games = []


def parse_puzzle_input(puzzle_input):
    result = []
    with open(puzzle_input) as file:
        for line in file.read().splitlines():
            result.append(CubeGame(line))

    return result


if __name__ == '__main__':
    games = parse_puzzle_input("./input.txt")

    part_1 = 0
    for game in games:
        part_1 += game.id if game.is_valid(12, 13, 14) else 0

    print(part_1)

    part_2 = sum([g.fewest_possible_powers() for g in games])

    print(part_2)


