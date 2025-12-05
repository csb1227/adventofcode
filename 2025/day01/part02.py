from input_reader import input_reader

instructions = input_reader.read_input("input.txt")

numeric_instructions = [input_reader.make_turn(x) for x in instructions]

position = 1000000000 + 50

zeros = 0
for instruction in numeric_instructions:
    for p in range(abs(instruction)):
        if instruction < 0:
            position -= 1
        else:
            position += 1

        if abs(position) % 100 == 0:
            zeros += 1

print(zeros)
