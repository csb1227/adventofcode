import re
from typing import List, Tuple


def read_input(file_path: str) -> tuple[list[list[str]], list[list[str]]]:
    with open(file_path, 'r') as f:
        _rules_raw, _sequences_raw = f.read().split('\n\n')

        # _rules = [[int(y) for y in x] for x in [rule.split("|") for rule in _rules_raw.split('\n')]]
        _rules = [rule.split("|") for rule in _rules_raw.split('\n')]

        # _sequences = [[int(y) for y in x] for x in [sequence.split(",") for sequence in _sequences_raw.split('\n')]]
        _sequences = [sequence.split(",") for sequence in _sequences_raw.split('\n')]

        return _rules, _sequences

def get_applicable_rules(rules: list[list[str]], sequence: list[str]) -> list[list[str]]:
    _applicable_rules = []

    for rule in rules:
        if all([x in sequence for x in rule]):
            _applicable_rules.append(rule)

    return _applicable_rules

def evaluate_rule(applicable_rule, sequence):
    pattern = f"{applicable_rule[0]}(?:,[0-9]{{{2}}})*,{applicable_rule[1]}"

    match = re.findall(pattern, ",".join(sequence))

    if not match:
        return False

    return True


def evaluate_rules(sequences, rules):
    valid_sequences = []
    invalid_sequences = []

    for sequence in sequences:
        applicable_rules = get_applicable_rules(rules, sequence)

        valid_sequence = True

        for applicable_rule in applicable_rules:
            checks_out = evaluate_rule(applicable_rule, sequence)

            if not checks_out:
                invalid_sequences.append(sequence)
                valid_sequence = False
                break

        if valid_sequence:
            valid_sequences.append(sequence)

    return valid_sequences, invalid_sequences