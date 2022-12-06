def open_buffer(b):
    with open(b, 'r') as f:
        return f.read()


def chunk_list(l, n):
    for i in range(0, len(l) - n+1):
        yield l[i:i + n]


def find_marker(b, c):
    fours = [f for f in chunk_list(b, c)]
    packet_sets = [set(f) for f in fours]

    i = 0
    for ps in packet_sets:
        if len(ps) == c:
            break
        i += 1

    return b.find(fours[i]) + c


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle_input.txt'

    print(f'Part 1: {find_marker(open_buffer(puzzle_input), 4)}')
    print(f'Part 2: {find_marker(open_buffer(puzzle_input), 14)}')
