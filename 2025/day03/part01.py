from input_reader import read_input

battery_banks = read_input("input.txt")

print(battery_banks)

def next_max_joltage(bank):
    if len(bank) == 1:
        return bank[0], 0
    next_max = max([int(x) for x in bank])
    next_max_index = bank.find(str(next_max))

    return next_max, next_max_index

total_jolts = []

for battery_bank in battery_banks:
    first_max, first_max_index = next_max_joltage(battery_bank[:-1])

    second_max, second_max_index = next_max_joltage(battery_bank[first_max_index + 1:])

    joltage = int(f"{first_max}{second_max}")

    total_jolts.append(joltage)

print(sum(total_jolts))

