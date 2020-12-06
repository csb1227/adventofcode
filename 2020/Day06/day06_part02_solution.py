from collections import Counter

customs_input = None
with open('input.txt', 'r') as f:
  customs_input = [[q for q in p.split('\n')] for p in f.read().split('\n\n')]

def getKeyByVal(x, val):
  keys = []
  for k,v in x.items():
    if v == val:
      keys.append(k)
  return keys

sum_counts = 0
for ci in customs_input:
  passenger_answers = Counter()
  for c in ci:
    for x in c:
      passenger_answers[x] += 1

  all_answered = getKeyByVal(dict(passenger_answers), len(ci))
  sum_counts += len(all_answered)

print(sum_counts)