import numpy as np
from collections import Counter

input = None
with open('input.txt', 'r') as f:
  input = [int(c) for c in f.read().split(',')]

lanternFish = Counter(input)

nextDay = Counter()
day = 0
nextDay = Counter()
while day <= 255:
  newFish= lanternFish[0]
  for d in range(8):
    nextDay[d] = lanternFish[d+1]
  nextDay[6] += newFish
  nextDay[8] = newFish
  day += 1
  lanternFish = nextDay

print(sum(lanternFish.values()))