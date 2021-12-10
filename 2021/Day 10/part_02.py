from collections import Counter
from queue import LifoQueue

data = [row for row in open('input.txt').read().split('\n') ]

openers = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

points = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

counts = {
  ')': 0,
  ']': 0,
  '}': 0,
  '>': 0
}

scores = []

for row in data:
  oStack = LifoQueue()
  rowIsCorrupt = False
  score = 0
  for d in row:
    if d in openers.keys():
      oStack.put(d)
    else:    
      o = oStack.get()
      if d != openers[o]:
        rowIsCorrupt = True
  if rowIsCorrupt:
    pass
  elif oStack.qsize() != 0:
    completionClosers = []
    while oStack.qsize() > 0:
      completionClosers.append(openers[oStack.get()])
    for cc in completionClosers:
      score = (score * 5) + points[cc]

    scores.append(score)
  else:
    print('Row is ok:      {}'.format(row))

scores = sorted(scores)
print(scores[int((len(scores)-1)/2)])