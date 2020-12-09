import itertools

data = [int(x.strip()) for x in open('input.txt').readlines()]
preamble = 25

def contiguousCombinations(x, target):
  n = len(x)
  indices = list(range(n+1))
  for i,j in itertools.combinations(indices, 2):
    if target == sum(x[i:j]) and len(x[i:j]) > 1:
      yield sorted(x[i:j])

for i in range(preamble, len(data)):
  if not any([data[i] == sum(x) for x in itertools.combinations(data[i-preamble:i], 2)]):
    print(data[i]) # part 1
    target = data[i]
    break

for c in contiguousCombinations(data, target):
  print(c[0] + c[-1]) # part 2