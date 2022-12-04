def make_assignments_ranges(x, i=0):
    result = []
    for assignment in x:
        a_as_range = []
        for a in assignment:
            a_as_range.append(range(a[0], a[1] + i, 1))
        result.append(a_as_range)

    return result


def open_assignments(x):
    with open(x, 'r') as f:
        pairs = [p for p in f.read().split('\n')]
        assignments = [a.split(',') for a in pairs]
        assignment_range = []
        for a in assignments:
            ar = [ar.split('-') for ar in a]
            ar_int = []
            for y in ar:
                ar_int.append([int(z) for z in y])
            assignment_range.append(ar_int)

        return assignment_range


def contained_assignments(assignments):
    contained_assignment_count = 0
    for assignment in assignments:
        a_as_range = []
        for a in assignment:
            a_as_range.append(range(a[0], a[1], 1))
        if ((a_as_range[0].start >= a_as_range[1].start and a_as_range[0].stop <= a_as_range[1].stop) or
                (a_as_range[1].start >= a_as_range[0].start and a_as_range[1].stop <= a_as_range[0].stop)):
            contained_assignment_count += 1
    return contained_assignment_count


def overlapping_assignments(assignments):
    overlapping_assignment_count = 0
    a = make_assignments_ranges(assignments, 1)
    for ar in a:
        print(ar)
        print(set(ar[0]) & set(ar[1]))
        if len(set(ar[0]) & set(ar[1])) > 0:
            overlapping_assignment_count += 1

    return overlapping_assignment_count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    example = open_assignments('./input/example.txt')
    puzzle_input = open_assignments('./input/input.txt')

    print(f"Part 1: {contained_assignments(puzzle_input)} fully contained assignment(s).")
    print(f"Part 2: {overlapping_assignments(puzzle_input)} overlapping assignment(s).")


# 224 too low
# 698 too low
