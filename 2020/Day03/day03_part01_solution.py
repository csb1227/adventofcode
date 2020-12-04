slope = None
with open('slope.txt', 'r') as f:
  slope = [[t for t in s] for s in f.read().split('\n')]

width = len(slope[0])
coordinates = []

y=0
x=0
while y < len(slope):  
  coordinates.append((y,x))
  x+=1
  y+=2

trees = 0
for (y,x) in coordinates:
  if slope[y][x%width] == '#':
    trees+=1

print(trees)



#1,1 57
#3,1 193
#5,1 64
#7,1 55
#1,2 35