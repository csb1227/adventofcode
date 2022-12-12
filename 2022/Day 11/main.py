import math

class Me(object):
    def __init__(self):
        self.worry_level = 0

    def worry(self, worry_factor, worry_operation):
        if worry_operation == '*':
            self.worry_level *= worry_factor if worry_factor else self.worry_level
        elif worry_operation == '+':
            self.worry_level += worry_factor if worry_factor else self.worry_level

    def relief(self):
        self.worry_level /= 3
        # need to round this down too


class Monkey(object):
    def __init__(self, mid, items, worry_factor, worry_operation, test_factor, test_target_true, test_target_false):
        self.id = mid
        self.items = items
        self.worry_factor = int(worry_factor) if worry_factor != 'old' else None
        self.worry_operation = worry_operation
        self.test_factor = test_factor
        self.test_target_true = test_target_true
        self.test_target_false = test_target_false
        self.inspected_items = 0

    def __repr__(self):
        return f'Monkey {self.id}: {self.inspected_items}'

    def inspect_item(self, relief):
        worry_level = self.items.pop(0)
        # print(worry_level)
        self.inspected_items += 1
        factor = worry_level if not self.worry_factor else self.worry_factor
        # print(factor)
        if self.worry_operation == '+':
            worry_level += factor
        elif self.worry_operation == '*':
            worry_level *= factor

        # print(worry_level)
        if relief > 1:
            worry_level = int(worry_level / relief)
        # print(worry_level)
        if worry_level % self.test_factor == 0:
            # print(f'Throw to {self.test_target_true}: {worry_level}')
            # print(self.items)
            # input()
            return self.test_target_true, worry_level
        else:
            # print(f'Throw to {self.test_target_false}: {worry_level}')
            # print(self.items)
            # input()
            return self.test_target_false, worry_level

    def throw(self):
        pass

    def catch(self, item):
        self.items.append(item)


def keep_away(rounds, monkeys, relief):
    for round in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                target, the_item = monkey.inspect_item(relief)
                monkeys[target].catch(the_item)

def monkey_business(monkeys, n):
    sorted_mb = list(reversed(sorted([monkey.inspected_items for monkey in monkeys])))

    return math.prod(sorted_mb[:n])


def open_input(x):
    with open(x, 'r') as f:
        return f.read()


def parse_input(x):
    for monkey in x.split('\n\n'):
        monkey_attributes = [ma.strip() for ma in monkey.split('\n')]
        yield Monkey(
            int(monkey_attributes[0][7]),
            [int(i) for i in monkey_attributes[1][16:].split(', ')],
            monkey_attributes[2][23:],
            monkey_attributes[2][21],
            int(monkey_attributes[3][19:]),
            int(monkey_attributes[4][25:]),
            int(monkey_attributes[5][26:])
        )


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    raw_instructions = open_input(example_input)
    monkeys_1 = list(parse_input(raw_instructions))
    monkeys_2 = list(parse_input(raw_instructions))

    # for monkey in monkeys:
    #     print(monkey)

    keep_away(20, monkeys_1, 3)

    # for monkey in monkeys_1:
    #     print(monkey)

    print(f'Part 1: {monkey_business(monkeys_1, 2)}')

    # keep_away(1000, monkeys_2, 1)
    # for monkey in monkeys_2:
    #     print(monkey)
    #
    # print(monkey_business(monkeys_2, 2))
