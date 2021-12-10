import numpy as np

data = [[cell for cell in row] for row in open('input.txt').read().split('\n') ]
dataMatrix = np.matrix(data)

def get_adjacent_indices(i, j, shape):
  m = shape[0]
  n = shape[1]
  adjacent_indices = []
  if i > 0:
    adjacent_indices.append((i-1,j))
  if i+1 < m:
    adjacent_indices.append((i+1,j))
  if j > 0:
    adjacent_indices.append((i,j-1))
  if j+1 < n:
    adjacent_indices.append((i,j+1))
  return adjacent_indices

def is_lowest_point(value, adjacent):
  if all(value < dataMatrix[i[0], i[1]] for i in adjacent):
    return True
  else:
    return False


shape = dataMatrix.shape
rows = list(range(dataMatrix.shape[0]))
cols = list(range(dataMatrix.shape[1]))

indices = {}
for m in rows:
  for n in cols:
    indices[(m, n)] = {
      'value': dataMatrix[m,n],
      'adjacent': get_adjacent_indices(m, n, shape),
      'low': False
    }

lowPoints = {}
for index, attributes in indices.items():
  if is_lowest_point(attributes['value'], attributes['adjacent']):
    lowPoints[index] = int(attributes['value'])

basins = {}

for lP in lowPoints:
  basin = set()
  nextEval = []
  toBeEval = [lP]
  doneEval = []
  while len(toBeEval) != 0:
    # print('To Evaluate: {}'.format(toBeEval))
    # print('Done       : {}'.format(doneEval))
    # print('Basin      : {}'.format(basin))
    index = toBeEval[0]
    if dataMatrix[index[0], index[1]] != '9':
      basin.add(index)
    
    doneEval.append(index)
    toBeEval.remove(index)
    toBeEval += [i for i in get_adjacent_indices(index[0], index[1], shape) if i not in doneEval and dataMatrix[i[0], i[1]] != '9']

  basins[lP] = basin

basinSizes = []
for basin in basins:
  basinSizes.append(len(basins[basin]))

basinSizes = sorted(basinSizes)

print(np.prod(basinSizes[-3:]))