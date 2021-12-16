import numpy as np
data = [[int(point) for point in row.split(',')] for row in open('input.txt').read().split('\n')]

folds = [row[11:].split('=') for row in [row for row in open('folds.txt').read().split('\n')]]

extentX = max([int(x[1]) for x in folds if x[0] == 'x']) * 2
extentY = max([int(y[1]) for y in folds if y[0] == 'y']) * 2

# because of 0
extentX += 1
extentY += 1

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
    if leftHalf.size == rightHalf.size:
      newThing = leftHalf + rightHalf
    elif leftHalf.size < rightHalf.size:
      newThing = rightHalf
      # start at the bottom
      i = -1
      for row in range(len(leftHalf)):
        for col in leftHalf[row]:
          newThing[i] += leftHalf[i]
          i -= 1
    elif leftHalf.size > rightHalf.size:
      newThing = leftHalf
      # start at the bottom
      i = -1
      for row in range(len(rightHalf)):
        for col in rightHalf[row]:
          newThing[i] += leftHalf[i]
          i -= 1

    instructions = newThing

  elif fold[0] == 'y':
    foldY = int(fold[1])
    # for y folds
    topHalf = instructions[:foldY]
    #reverse it cuz we're flipping it up
    bottomHalf = np.flip(instructions[foldY+1:], axis=0)

    # perform the folds
    # if the top half is smaller or the same size as bottom
    if topHalf.size == bottomHalf.size:
      newThing = topHalf + bottomHalf
    elif topHalf.size < bottomHalf.size:
      newThing = bottomHalf
      # start at the bottom
      i = -1
      for n in range(len(topHalf)):
        newThing[i] += topHalf[i]
        i -=1
    elif topHalf.size > bottomHalf.size:
      newThing = topHalf
      # start at the bottom
      i = -1
      for n in range(len(bottomHalf)):
        newThing[i] += topHalf[i]
        i -=1

    instructions = newThing

instructions = np.where(instructions > 0, '▒', instructions)
instructions = np.where(instructions == '0', ' ', instructions)

for i in instructions:
  print(''.join(i))
