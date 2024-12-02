from engine import Engine


def parse_puzzle_input(puzzle_input):
    result = []
    with open(puzzle_input) as file:
        [result.append(line) for line in file.read().split("\n")]

    return result


if __name__ == '__main__':
    engine = Engine(parse_puzzle_input("./input.txt"))

    possible_engine_parts = engine.find_possible_part_numbers()
    part_numbers = engine.identify_engine_parts(possible_engine_parts)

    print(sum(part_numbers))

    # 530002 -- too low
