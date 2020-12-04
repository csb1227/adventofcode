expenseReport = None
with open('expense_report.txt', 'r') as f:
  expenseReport = [int(e) for e in f.read().split('\n')]

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


