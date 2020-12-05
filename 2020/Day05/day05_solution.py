import numpy as np

boardingPass_input = None
with open('input.txt', 'r') as f:
  boardingPass_input = [bp for bp in f.read().split('\n')]

def parseBoardingPass(seatId):
  rowInput = seatId[:7]
  colInput = seatId[7:]

  row = None
  rows = list(range(0,128))
  for r in rowInput:
    if r == 'F':
      rows = rows[:int(len(rows)/2)]
    elif r == 'B':
      rows = rows[int(len(rows)/2):]

  row = rows[0]

  col = None
  cols = list(range(0,8))
  for c in colInput:
    if c == 'L':
      cols = cols[:int(len(cols)/2)]
    elif c == 'R':
      cols = cols[int(len(cols)/2):]

  col = cols[0]

  seat = row * 8 + col

  return seat

maxSeat = 0
takenSeats = []
for bP in boardingPass_input:
  x = parseBoardingPass(bP)
  takenSeats.append(x)
  maxSeat = x if x > maxSeat else maxSeat

allSeats = list(range(min(takenSeats), max(takenSeats)+1))

print(np.setdiff1d(allSeats, takenSeats))

