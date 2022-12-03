data = [int(y) for y in [x.split(',') for x in open('input.txt').readlines()][0]]
data[1] = 12
data[2] = 2

j = 0
computing = True
while computing:
  try:
    if data[j] == 1:
      data[data[j+3]] = data[data[j+1]] + data[data[j+2]]
      j += 4
    elif data[j] == 2:
      data[data[j+3]] = data[data[j+1]] * data[data[j+2]]
      j += 4
    elif data[j] == 99:
      computing = False
  except IndexError:
    computing = False

print(data[0])
