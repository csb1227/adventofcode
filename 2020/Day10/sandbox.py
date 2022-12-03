import itertools
from collections import Counter

data = [int(x.strip()) for x in open('input.txt').readlines()]
#data = [16,10,15,5,1,11,7,19,6,12,4]

def part2(nums):
  jolts = sorted(nums)
  jolts.append(jolts[-1] + 3)

  print(jolts)

  dp = Counter()
  dp[0] = 1

  for jolt in jolts:
    print(dp)
    print(dp[jolt - 1], ' + ', dp[jolt - 2], ' + ', dp[jolt - 3])
    
    dp[jolt] = dp[jolt - 1] + dp[jolt - 2] + dp[jolt - 3]

  return dp[jolts[-1]]

print(part2(data))