import numpy as np
data = [[int(point) for point in row.split(',')] for row in open('input.txt').read().split('\n')]

folds = [row[11:].split('=') for row in [row for row in open('folds.txt').read().split('\n')]]

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

# for each fold in the folding instructions
for fold in folds:
  newThing = None
  if fold[0] == 'x':
    foldX = int(fold[1])
    # for x folds
    leftHalf = np.array([row[:foldX] for row in instructions])
    #reverse it cuz we're flipping it left
    rightHalf = np.flip(np.array([row[foldX+1:] for row in instructions]), axis=1)

    # perform the folds
    # if the top half is smaller or the same size as bottom
    if len(leftHalf) == len(rightHalf):
      newThing = leftHalf + rightHalf
    elif len(leftHalf) < len(rightHalf):
      newThing = rightHalf.copy()
      # start at the bottom
      i = -1
      for n in range(len(leftHalf)):
        newThing[i] += leftHalf[i]
        i -=1
    elif len(leftHalf) > len(rightHalf):
      newThing = leftHalf.copy()
      # start at the bottom
      i = -1
      for n in range(len(rightHalf)):
        newThing[i] += leftHalf[i]
        i -=1

    instructions = newThing.copy()

  elif fold[0] == 'y':
    foldY = int(fold[1])
    # for y folds
    topHalf = instructions[:foldY]
    #reverse it cuz we're flipping it up
    bottomHalf = np.flip(instructions[foldY+1:], axis=0)

    # perform the folds
    # if the top half is smaller or the same size as bottom
    if len(topHalf) == len(bottomHalf):
      newThing = topHalf + bottomHalf
    elif len(topHalf) < len(bottomHalf):
      newThing = bottomHalf.copy()
      # start at the bottom
      i = -1
      for n in range(len(topHalf)):
        newThing[i] += topHalf[i]
        i -=1
    elif len(topHalf) > len(bottomHalf):
      newThing = topHalf.copy()
      # start at the bottom
      i = -1
      for n in range(len(bottomHalf)):
        newThing[i] += topHalf[i]
        i -=1

    instructions = newThing.copy()

  break




print(np.count_nonzero(instructions))
