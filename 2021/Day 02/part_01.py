instructions = None
with open('input.txt', 'r') as f:
  instructions = [i.split(' ') for i in f.read().split('\n')]

# print(instructions)

forward = 0
up = 0
down = 0

for i in instructions:
  if i[0] == 'forward':
    forward += int(i[1])
  elif i[0] == 'up':
    up -= int(i[1])
  else:
    down += int(i[1])

print(forward * (up + down))