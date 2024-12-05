from aoc_methods import read_input, evaluate_rules

rules, sequences = read_input('input/actual.txt')

valid_sequences, _ = evaluate_rules(sequences, rules)

result = 0

for valid_sequence in valid_sequences:
    x = len(valid_sequence) // 2
    result += int(valid_sequence[x])

print(result)