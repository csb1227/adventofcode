customs_input = None
with open('input.txt', 'r') as f:
  customs_input = [[q for q in p.split('\n')] for p in f.read().split('\n\n')]

sum_counts = 0
for ci in customs_input:
  unique_answers = []
  for c in ci:
    unique_answers = list(set(unique_answers) | set(c))
  sum_counts += len(unique_answers)

print(sum_counts)
  