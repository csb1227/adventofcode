import math


class Item(object):
    def __init__(self, original, monkey):
        self.original = original
        self.current = original
        self.monkey = monkey


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

    def state(self):
        return f'Monkey {self.id}:\n' \
               f'  Starting items : {", ".join([str(i.original) for i in self.items])}\n' \
               f'  Operation: new = old {self.worry_operation} {self.worry_factor if self.worry_factor else "old"}\n' \
               f'  Test: divisible by {self.test_factor}\n' \
               f'    If true: throw to monkey {self.test_target_true}\n' \
               f'    If false: throw to monkey {self.test_target_false}\n'

    def inspect_item(self, relief, gcd):
        item = self.items.pop(0)

        self.inspected_items += 1

        factor = item.current if not self.worry_factor else self.worry_factor
        if self.worry_operation == '+':
            item.current += factor
        elif self.worry_operation == '*':
            item.current *= factor

        if relief:
            item.current = item.current // relief

        if gcd:
            item.current = item.current % gcd

        if item.current % self.test_factor == 0:
            return self.test_target_true, item
        else:
            return self.test_target_false, item

    def throw(self):
        pass

    def catch(self, item):
        self.items.append(item)


def keep_away(rounds, monkeys, relief=None, gcd=None):
    for round in range(rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                target, the_item = monkey.inspect_item(relief, gcd)
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
        test_factor = int(monkey_attributes[3][19:])
    for monkey in x.split('\n\n'):
        monkey_attributes = [ma.strip() for ma in monkey.split('\n')]
        yield Monkey(
            int(monkey_attributes[0][7]),
            [Item(int(i), int(monkey_attributes[0][7])) for i in monkey_attributes[1][16:].split(', ')],
            monkey_attributes[2][23:],
            monkey_attributes[2][21],
            int(monkey_attributes[3][19:]),
            int(monkey_attributes[4][25:]),
            int(monkey_attributes[5][26:])
        )


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    raw_instructions = open_input(puzzle_input)
    monkeys_1 = list(parse_input(raw_instructions))
    monkeys_2 = list(parse_input(raw_instructions))

    keep_away(20, monkeys_1, 3)
    #
    print(f'Part 1: {monkey_business(monkeys_1, 2)}')

    gcd = 1
    for monkey in monkeys_2:
        gcd *= monkey.test_factor
    keep_away(10000, monkeys_2, 0, gcd)

    print(f'Part 2: {monkey_business(monkeys_2, 2)}')
