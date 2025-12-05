from input_reader import input_reader

instructions = input_reader.read_input("input.txt")

numeric_instructions = [input_reader.make_turn(x) for x in instructions]

position = 50
zeros = 0

for instruction in numeric_instructions:
    _, position = divmod(position + instruction, 100)
    if position == 0:
        zeros += 1

print(zeros)
