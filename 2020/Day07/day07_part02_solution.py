import re

baggage_rules = None
with open('input.txt', 'r') as f:
  baggage_rules = [b for b in f.read().split('\n')]

bag_rules = []

for b in baggage_rules:
  bag_rules.append(re.split('\sbags?\scontain\s|\sbags?,|\sbags?.', b)[:-1])

bag_rules_dict = {}
for r in bag_rules:
  bag_rules_dict[r[0]] = [u.replace('no other', '1 no other').strip() for u in r[1:]]

shiny_rule = [s.strip() for s in [r for r in bag_rules if r[0] == 'shiny gold'][0]][1:]

def count_bags(x, bag_total=0):  
  for r in x:
    if r[2:] != 'no other':
      bag_total += int(r[0]) + (int(r[0]) * count_bags(bag_rules_dict[r[2:]]))
    else:
      bag_total += 0
  
  return bag_total

print(count_bags(shiny_rule, 0))
