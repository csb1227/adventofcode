item_priority = {}
for ip in range(26):
    item_priority[chr(ip + 97)] = ip + 1
    item_priority[chr(ip + 65)] = ip + 27


def chunk_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def open_rucksacks(r):
    _rucksacks = None
    with open(r, 'r') as f:
        _rucksacks = [i for i in f.read().split('\n')]

    return _rucksacks


def find_bad_item(r):
    compartment_size = int(len(r)/2)
    compartment_1 = list(set(r[:compartment_size]))
    compartment_2 = list(set(r[compartment_size:]))

    bad_item = [i for i in compartment_1 if i in compartment_2]

    return item_priority[bad_item[0]]


def part_01(r):
    priority_sum = 0

    for sack in r:
        priority_sum += find_bad_item(sack)

    print(priority_sum)


def part_02(r):
    groups = chunk_list(r, 3)

    priority_sum = 0

    for g in groups:
        r1 = set(g[0])
        r2 = set(g[1])
        r3 = set(g[2])
        common_item = [i for i in r1 if i in r2 and i in r3]

        priority_sum += item_priority[common_item[0]]

    print(priority_sum)


if __name__ == '__main__':
    example = open_rucksacks('./input/example.txt')
    rucksacks = open_rucksacks('./input/puzzle_input.txt')

    part_01(rucksacks)
    part_02(rucksacks)
    