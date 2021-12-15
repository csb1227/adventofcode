import numpy as np
from queue import LifoQueue

data = [[int(cell) for cell in row] for row in open('input.txt').read().split('\n') ]
octoMatrix = np.matrix(data)


def get_adjacent_indices(row, col, shape):
  mRow = shape[0]
  nCol = shape[1]
  adjacent_indices = []

  # Up
  if row > 0:
    adjacent_indices.append((row-1,col))

  # Up and Right
  if row > 0 and col+1 <nCol:
    adjacent_indices.append((row-1, col+1))

  # Right
  if col+1 < nCol:
    adjacent_indices.append((row,col+1))

  # Right and Down
  if col+1 < nCol and row+1 < mRow:
    adjacent_indices.append((row+1, col+1))

  # Down
  if row+1 < mRow:
    adjacent_indices.append((row+1,col))

  # Down and Left
  if row+1 < mRow and col > 0:
    adjacent_indices.append((row+1, col-1))

  # Left
  if col > 0:
    adjacent_indices.append((row,col-1))

  # Left and Up
  if row > 0 and col > 0:
    adjacent_indices.append((row-1, col-1))

  return adjacent_indices

# keep track of how many flashes there are
flashes = 0

print(octoMatrix)
print('------------------------------------------')

i = 0
bigFlash = False
while not bigFlash:
  # every octopus engergy goes up 1
  octoMatrix += 1
  # only let each octopus flash at most once
  flashedThisCycle = []

  # get initial set of octopus to flash
  flashQueue = LifoQueue()
  for o in np.argwhere(octoMatrix > 9):
    flashes += 1
    flashQueue.put(o)
    flashedThisCycle.append((o[0], o[1]))
  
  # as long as there are octopus to flash
  while flashQueue.qsize() > 0:
    # get an octo to flash
    flashOcto = flashQueue.get()
    # mark that octo as having flashed this cycle
    flashedThisCycle.append((flashOcto[0], flashOcto[1]))
    # get adjacent octos
    adjacentOctos =  get_adjacent_indices(flashOcto[0], flashOcto[1], octoMatrix.shape)

    # print(flashOcto, adjacentOctos)
    # each adjacent octo gets energy +1
    for aO in adjacentOctos:
      octoMatrix[aO] += 1

    # check if any new octopus need to be flashed but only if they haven't already
    for o in [newO for newO in np.argwhere(octoMatrix > 9) if (newO[0], newO[1]) not in flashedThisCycle]:
      flashes += 1
      flashQueue.put(o)
      flashedThisCycle.append((o[0], o[1]))

  if np.all(octoMatrix > 9):
    bigFlash = True
  
  octoMatrix[octoMatrix > 9] = 0
  

  i += 1

print('------------------------------------------')
print(octoMatrix)
print('Big flash on cycle {}'.format(i))

# 5003 too high