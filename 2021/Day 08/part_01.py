
data = [[l.split(' ') for l in line.split(' | ')] for line in open('input.txt').read().split('\n') ]

outputValues = []
for d in data:
  outputValues.append(d[1])

i = 0
for v in outputValues:
  for w in v:
    i += 1 if len(w) in [2, 4, 3, 7] else 0

print(i)