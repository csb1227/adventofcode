from collections import Counter

polyTemplate, insertionRules = open('input.txt').read().split('\n\n')

insertionRules = {k:v for k,v in [row.split(' -> ') for row in insertionRules.split('\n')]}

assertions = {int(k[-1:].replace('e', '0')):v.strip() for k,v in [row.split(': ') for row in open('assertion.txt').read().split('\n')]}


insertionStep = ''
s = 0
steps = 10
while s < steps:
  insertionStep = ''
  for i in range(len(polyTemplate)-1):
    insertionStep += polyTemplate[i] + insertionRules[polyTemplate[i]+polyTemplate[i+1]]
    if i == len(polyTemplate)-2:
      insertionStep += polyTemplate[-1]

  s += 1
  polyTemplate = insertionStep
  

# print(Counter(polyTemplate))
print(Counter(polyTemplate).most_common()[0][1] - Counter(polyTemplate).most_common()[-1][1])

# only a couple resluts provided
# try:
#   if polyTemplate != assertions[steps]:
#     print('{} does not equal {}'.format(polyTemplate, assertions[steps]))
#   else:
#     print(polyTemplate)
# except:
#   pass