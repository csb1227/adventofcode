instructions = None
with open('input.txt', 'r') as f:
  instructions = [i.split(' ') for i in f.read().split('\n')]

aim = 0
horizontal = 0
depth = 0

for i in instructions:
  if i[0] == 'forward':
    horizontal += int(i[1])
    depth += aim * int(i[1])
  elif i[0] == 'up':
    aim -= int(i[1])
  else:
    aim += int(i[1])

print(horizontal * depth)