import numpy as np

calls = None
with open('calls.txt', 'r') as f:
  calls = [int(c) for c in f.read().split(',')]

boards = None
with open('boards.txt', 'r') as f:
  boards = [np.array([[int(k) for k in j.split(' ') if k != ''] for j in i.split('\n')]) for i in f.read().split('\n\n')]

called = []
winningBoard = None
for call in calls:
  called.append(call)
  winner = False
  for board in boards:
    for c in range(5): # cuz there's 5 rows and 5 columns on a board
      if all(x in called for x in board[c]):
        winner = True
      if all(y in called for y in board[:,c]):
        winner = True
      if winner:
        break
    if winner:
      winningBoard = board
      break
  if winner:
    break

notCalledOnBoard = []
for r in winningBoard:
  for c in r:
    if c not in called:
      notCalledOnBoard.append(c)

print(winningBoard)
print(called)
print(sum(notCalledOnBoard) * called[-1])