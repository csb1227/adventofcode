from input_reader import read_input, eliminate_impossible_ranges, eliminate_impossible_parts_of_ranges

valid_ranges = read_input("input.txt")

possible_ranges = eliminate_impossible_ranges(valid_ranges)

possible_ranges = eliminate_impossible_parts_of_ranges(possible_ranges)

invalids = set()

for begin, end in possible_ranges:
    repeat_len = len(begin) // 2

    half_begin = int(begin[:repeat_len])
    half_end = int(end[:repeat_len])

    begin_int, end_int = int(begin), int(end)

    for x in range(half_begin, half_end + 1):
        y = int(f"{x}{x}")
        if begin_int <= y <= end_int:
            invalids.add(y)

print(sum(invalids))