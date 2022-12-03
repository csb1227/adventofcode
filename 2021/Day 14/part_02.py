from collections import Counter, defaultdict

polyTemplateInput, insertionRulesInput = open('input.txt').read().split('\n\n')

insertionRules = {k:[str(k[0] + v + k[1])[:2], str(k[0] + v + k[1])[1:]] for k,v in [row.split(' -> ') for row in insertionRulesInput.split('\n')]}

# polyTemplate = Counter()
polyTemplate = defaultdict(int)

# the initial pairs
for i in range(len(polyTemplateInput)-1):
  polyTemplate[polyTemplateInput[i] + polyTemplateInput[i+1]] += 1


# the initial individual items
items = defaultdict(int)
for k,v in polyTemplate.items():
  items[k[0]] += 1 * v
items[polyTemplateInput[-1]] += 1

steps = 40
for _ in range(steps):
  newPoly = defaultdict(int)
  for k,v in polyTemplate.items():    
    p1 = insertionRules[k][0]
    p2 = insertionRules[k][1]

    newPoly[p1] += 1 * v
    newPoly[p2] += 1 * v

    items[p2[0]] += 1 * v

  polyTemplate = newPoly


print(max(items.values()) - min(items.values()))
