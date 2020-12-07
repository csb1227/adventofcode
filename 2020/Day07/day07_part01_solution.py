import re

baggage_rules = None
with open('input.txt', 'r') as f:
  baggage_rules = [b for b in f.read().split('\n')]

bag_rules = []

for b in baggage_rules:
  bag_rules.append(re.split('\sbags?\scontain\s[0-9]\s|\sbags?,\s[0-9]\s|\sbags?.', b)[:-1])

goes_in = []

def bag_search(x):
  for r in bag_rules:
    if x in r and x != r[0]:
      goes_in.append(r[0])
      bag_search(r[0])
    else:
      pass
  return

bag_search('shiny gold')

print(len(set(goes_in)))