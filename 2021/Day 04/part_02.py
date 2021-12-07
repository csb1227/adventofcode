import numpy as np

calls = None
with open('calls.txt', 'r') as f:
  calls = [int(c) for c in f.read().split(',')]

boards = None
with open('boards.txt', 'r') as f:
  boards = [np.array([[int(k) for k in j.split(' ') if k != ''] for j in i.split('\n')]) for i in f.read().split('\n\n')]


winningBoard = None
winningCalled = []
for board in boards:
  winner = False
  called = []
  for call in calls:
    called.append(call)
    for c in range(5):
      if all(x in called for x in board[c]):
        winner = True
      if all(y in called for y in board[:,c]):
        winner = True
      if winner and len(called) > len(winningCalled):
        winningCalled = called
        winningBoard = board
        break
    if winner:
      break


notCalledOnBoard = []
for r in winningBoard:
  for c in r:
    if c not in winningCalled:
      notCalledOnBoard.append(c)

print(winningCalled)
print(winningBoard)
print(sum(notCalledOnBoard) * winningCalled[-1])