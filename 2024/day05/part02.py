from aoc_methods import read_input, evaluate_sequences, correct_invalid_sequences, \
    calculate_result

rules, sequences = read_input('input/actual.txt')

_, invalid_sequences = evaluate_sequences(sequences, rules)

corrected_sequences = correct_invalid_sequences(invalid_sequences, rules)

result = calculate_result(corrected_sequences)

print(result)