from input_reader import read_input, eliminate_impossible_ranges, eliminate_impossible_parts_of_ranges

valid_ranges = read_input("example.txt")

possible_ranges = eliminate_impossible_ranges(valid_ranges)

print(possible_ranges)

possible_ranges = eliminate_impossible_parts_of_ranges(possible_ranges)

print(possible_ranges)
invalids = set()
for rng in possible_ranges:
    begin = rng[0]
    end = rng[1]
    num_len = len(begin)
    repeat_len = int(num_len / 2)

    first_repeatable = begin[:repeat_len]

    half_max_begin = max(int(begin[:repeat_len]), int(begin[repeat_len:]))
    half_min_end = min(int(end[:repeat_len]), int(end[repeat_len:]))

    max_begin = int(f"{half_max_begin}{half_max_begin}")
    min_end = int(f"{half_min_end}{half_min_end}")

    if int(begin) <= max_begin <= int(end):
        invalids.add(max_begin)

    if int(begin) <= min_end <= int(end):
        invalids.add(min_end)



print(sum(invalids))

# 22380332142 too low
