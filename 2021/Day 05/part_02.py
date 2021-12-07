from collections import Counter

lines = None
with open('input.txt', 'r') as f:
  lines = [
    [[int(p) for p in pair.split(',')] for pair in [point for point in line.split(' -> ')]] for line in f.read().split('\n')]

x = []
for line in lines:
  start = line[0]
  end = line[-1]
  x.append(sorted(line))

points = []
for line in x:
  x1, y1 = line[0]
  x2, y2 = line[1]
  
  if x1 == x2:
    for y in range(y1, y2+1, 1):
      points.append((x1, y))
  elif y1 == y2:
    for x in range(x1, x2+1, 1):
      points.append((x, y1))
  else:
    for x in range(x1, x2+1, 1):
      slope = (y2 - y1)/(x2-x1)
      # print(x1, y1, x2, y2)
      points.append((x, int(slope*x - (slope*x1 - y1))))

print(len([p for p in Counter(points).most_common() if p[1] > 1]))