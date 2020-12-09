import copy
import re

data = [(lambda a,b : [a, b])(*re.findall('\+?\-?\w+', line)) for line in open('input.txt').readlines() ]

def compute(x):
  lineOp = 0
  lineCount = []
  accumulator = 0

  while lineOp not in lineCount:
    instruction = x[lineOp][0]
    lineCount.append(lineOp)
    if instruction == 'acc':
      accumulator += int(x[lineOp][1])
      lineOp += 1
    elif instruction == 'jmp':
      lineOp += int(x[lineOp][1])
    elif instruction == 'nop':
      lineOp += 1

    if lineOp == len(x):
      print('Last instruction before exit.')
      return True, accumulator

  return False, accumulator

lenData = len(data)
success = False
value = 0
for i in range(lenData):
  td = copy.deepcopy(data)
  if td[i][0] == 'nop':
    td[i][0] = 'jmp'
    success, value = compute(td)
  elif td[i][0] == 'jmp':
    td[i][0] = 'nop'
    success, value = compute(td)
  else:
    success, value = compute(td)

  if success:
    break

print(value)
