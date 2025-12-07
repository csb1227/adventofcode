def read_input(file_path: str):
    with open(file_path, "r") as file:
        product_id_ranges = file.read()
        return [[y for y in x.split("-")] for x in product_id_ranges.split(",")]


def eliminate_impossible_ranges(product_id_ranges) -> list:
    result = []
    for rng in product_id_ranges:
        if (len(rng[0]) == len(rng[1])) and len(rng[0]) % 2 != 0:
            pass
        else:
            result.append(rng)

    return result

def eliminate_impossible_parts_of_ranges(product_id_ranges) -> list:
    result = []
    for rng in product_id_ranges:
        first_len = len(rng[0])
        second_len = len(rng[1])
        if first_len % 2 != 0:
            first_possible_number = f"1{'0' * first_len}"
            result.append([first_possible_number, rng[1]])
        elif second_len % 2 != 0:
            second_possible_number = f"{'9' * (second_len - 1)}"
            result.append([rng[0], second_possible_number])
        else:
            result.append(rng)

    return result