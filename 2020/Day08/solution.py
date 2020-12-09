import re

data = [(lambda a,b : [a, b])(*re.findall('\+?\-?\w+', line)) for line in open('input.txt').readlines() ]

lineOp = 0
lineCount = []
accumulator = 0

while lineOp not in lineCount:
  instruction = data[lineOp][0]
  lineCount.append(lineOp)
  if instruction == 'acc':
    accumulator += int(data[lineOp][1])
    lineOp += 1
  elif instruction == 'jmp':
    lineOp += int(data[lineOp][1])
  elif instruction == 'nop':
    lineOp += 1


print(accumulator)
