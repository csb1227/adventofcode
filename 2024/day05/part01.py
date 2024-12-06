from aoc_methods import read_input, evaluate_sequences, calculate_result

rules, sequences = read_input('input/actual.txt')

valid_sequences, _ = evaluate_sequences(sequences, rules)

result = calculate_result(valid_sequences)

print(result)
