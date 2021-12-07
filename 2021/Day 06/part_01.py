import numpy as np

lanternFish = None
with open('input.txt', 'r') as f:
  lanternFish = np.array([int(c) for c in f.read().split(',')])

day = 0
while day <= 80:  
  lanternFish = np.append(lanternFish, [8] * np.count_nonzero(lanternFish == -1))
  lanternFish = np.where(lanternFish == -1, 6, lanternFish)
  lanternFish -= 1
  day += 1
  

print(len(lanternFish))