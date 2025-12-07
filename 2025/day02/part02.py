import re

from input_reader import read_input

valid_ranges = read_input("input.txt")

invalids = set()

def do_regex_stuff(length, number):
    pattern = rf"(^\d{{{length}}})\1+"
    match = re.fullmatch(pattern, str(number))
    if match:
        return True
    else:
        return False

for begin, end in valid_ranges:
    begin_int = int(begin)
    end_int = int(end)

    for x in range(begin_int, end_int + 1):
        if x in invalids:
            continue

        len_x = len(str(x))

        for i in range(1, 16):
            if len_x % i == 0:
                if do_regex_stuff(i, x):
                    invalids.add(x)

print(sum(invalids))