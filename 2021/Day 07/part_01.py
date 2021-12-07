from os import stat
import statistics
import numpy as np
from collections import Counter

crabSubs = None
with open('input.txt', 'r') as f:
  crabSubs = sorted([int(i) for i in f.read().split(',')])

crabSubMatrix = np.matrix(crabSubs)
print(np.absolute(crabSubMatrix - statistics.median(crabSubs)).sum())