from queue import PriorityQueue


def find_start_end(x):
    start = None
    end = None
    for ix_row, row in enumerate(x):
        for ix_col, col in enumerate(row):
            if x[ix_row][ix_col] == 83:
                start = (ix_row, ix_col)
            elif x[ix_row][ix_col] == 69:
                end = (ix_row, ix_col)

    return start, end


def parse_input(x):
    return [[ord(point) for point in row] for row in open(x).read().split('\n')]


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star_priority_queue(graph, start, end):
    open_list = PriorityQueue()
    closed_list = {start: None}

    distance_so_far = {start: 0}
    neighbor_offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    position = None

    # put the start into the queue
    open_list.put((0, start))

    while not open_list.empty():
        # get top priority (lowest risk) node from queue and blacklist it on closed_list
        position = open_list.get()[1]

        # you got to the end
        if position == end:
            break

        try:
            # for each neighbor of your current position
            for offset in neighbor_offsets:
                new_position = (position[0] + offset[0], position[1] + offset[1])
                # if the new position is on the map
                if 0 <= new_position[0] < len(graph) and 0 <= new_position[1] < len(graph[0]):
                    # calculate the distance for going to the new position
                    new_distance = distance_so_far[position] + 1
                    # if the new position is not black listed and you can reach it
                    if (new_position not in closed_list and graph[new_position[0]][new_position[1]] <= graph[position[0]][position[1]] + 1) or \
                            (new_position in distance_so_far.keys() and new_distance < distance_so_far[new_position]):
                        distance_so_far[new_position] = distance_so_far[position] + 1
                        priority = new_distance # + manhattan_distance(new_position, end)
                        open_list.put((priority, new_position))
                        closed_list[new_position] = position

        except IndexError:
            print(f'Error at: {new_position}')

    return distance_so_far[position]


if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    data = parse_input(puzzle_input)
    start, end = find_start_end(data)

    data[start[0]][start[1]] = ord('a')
    data[end[0]][end[1]] = ord('z')

    path = a_star_priority_queue(data, start, end)

    print(f'Part 1: {path}')

# 564 too high
# 538 too high
# 526 too low

