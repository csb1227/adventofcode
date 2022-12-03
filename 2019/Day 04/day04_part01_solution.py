from collections import Counter

# a non decreasing seed in the given range
seed = [ x for x in [ str(s) for s in range(254032, 789860+1) ] if x == ''.join(sorted(x)) ]

valids = []
for s in seed:
  thisSeed = Counter()
  for n in s:
    thisSeed.update(n)
  if any([True for x in thisSeed.values() if x >= 2]):
    valids.append(s)

print(len(valids))
