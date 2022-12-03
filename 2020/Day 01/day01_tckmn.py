from functools import reduce
import itertools
import operator

data = map(int, open('expense_report.txt').readlines())

# both parts
for n in [2, 3]:
    print(next(reduce(operator.mul, nums)
               for nums in itertools.combinations(data, n)
               if sum(nums) == 2020))