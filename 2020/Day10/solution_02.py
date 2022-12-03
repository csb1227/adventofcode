import itertools
from collections import Counter

#data = [int(x.strip()) for x in open('input.txt').readlines()]
data = [2,3,6,7,8,10]

def part2(nums):
  jolts = sorted(nums)
  jolts.append(jolts[-1] + 3)

  dp = Counter()
  dp[0] = 1

  for jolt in jolts:    
    dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]

  print(dp)
  return dp[jolts[-1]]

print(part2(data))