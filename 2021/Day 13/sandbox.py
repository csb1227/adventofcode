import numpy as np
data = [[int(point) for point in row.split(',')] for row in open('sample_input.txt').read().split('\n')]

foldY = 3
foldX = 5

extentX = 0
extentY = 0

for d in data:
  extentX = d[0] if d[0] > extentX else extentX
  extentY = d[1] if d[1] > extentY else extentY

# because of 0
extentX += 1
extentY += 1

# instructions = []
# for i in range(extentY):
#   instructions.append(np.array([0]*extentX))

instructions = np.array([[0]*extentX]*extentY)

for point in data:
  x = point[0]
  y = point[1]

  instructions[y][x] = 1

# for y folds
topHalf = instructions[:foldY]
#reverse it cuz we're flipping it up
bottomHalf = np.flip(instructions[foldY+1:], axis=0)

print(len(topHalf))
print(bottomHalf)

# 

print(topHalf + bottomHalf)