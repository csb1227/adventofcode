expenses = None
with open('expense_report.txt', 'r') as f:
  expenses = [int(e) for e in f.read().split('\n')]

def methodOne(expenseReport):
  print('methodOne')
  c = 0
  h = range(len(expenseReport))
  q = False

  for i in h:
    for j in h[i+1:]:
      c+=1
      s = expenseReport[i] + expenseReport[j]
      if s > 2020:
        continue
      other = 2020 - s
      if other in expenseReport:
        print(expenseReport[i], expenseReport[j], other, expenseReport[i] * expenseReport[j] * other)
        q = True
        break
    if q:
      break

  print(c)


def methodTwo(expenseReport):
  print('methodTwo')
  c = 0
  q = False

  for e in expenseReport:
    balance = 2020 - e
    for eR in expenseReport:
      c+=1
      b = balance - eR
      if b in expenseReport:
        print(e, eR, b, e*eR*b)
        q = True
        break
    if q:
      break


  print(c)


methodOne(expenses)
methodTwo(expenses)

methodOne(sorted([e for e in reversed(expenses)]))
methodTwo(sorted([e for e in reversed(expenses)]))