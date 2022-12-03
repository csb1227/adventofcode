from collections import Counter

data = [int(x.strip()) for x in open('input.txt').readlines()]

data = [x for x in reversed(sorted(data))]
data.append(data[0]+3)
data.append(0)
data = [x for x in reversed(sorted(data))]

notDone = True

diffs = Counter()
i = 0
while notDone:
  try:
    diffs.update([data[i] - data[i+1]])
  except IndexError:
    notDone = False
  i += 1

print(diffs)
print(diffs[1] * diffs[3])
