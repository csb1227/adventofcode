expenseReport = None
with open('expense_report.txt', 'r') as f:
  expenseReport = [int(e) for e in f.read().split('\n')]

possibles = {}

for e in expenseReport:
  pair = 2020 - e
  if pair in expenseReport:
    if e > pair:
      possibles[(e, pair)] = e * pair
    else:
      possibles[(pair, e)] = e * pair

print(possibles)


