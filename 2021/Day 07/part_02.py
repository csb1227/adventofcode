import pandas as pd

crabSubs = None
with open('input.txt', 'r') as f:
  crabSubs = sorted([int(i) for i in f.read().split(',')])

crabSubsDF = pd.DataFrame(crabSubs, columns=['Current Location'])

for i in range(min(crabSubs), max(crabSubs)+1, 1):
  crabSubsDF[i] = (0.5 * abs(crabSubsDF['Current Location']-i).pow(2)) - (0.5 * abs(crabSubsDF['Current Location']-i)) + abs(crabSubsDF['Current Location']-i)

print(min(crabSubsDF.sum(axis=0).drop(['Current Location'])))
