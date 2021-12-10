from queue import LifoQueue

data = [row for row in open('input.txt').read().split('\n') ]

openers = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

points = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

counts = {
  ')': 0,
  ']': 0,
  '}': 0,
  '>': 0
}

oStack = LifoQueue()

for row in data:
  for d in row:
    if d in openers.keys():
      oStack.put(d)
    else:    
      o = oStack.get()
      if d != openers[o]:
        #print('Expected {} but found {} instead.'.format(openers[o], d))
        counts[d] += 1


print(sum([points[c]*counts[c] for c in counts]))