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


print(sum([v+1 for v in lowPoints.values()]))


