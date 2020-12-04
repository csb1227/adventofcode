passwords = None
with open('passwords.txt', 'r') as f:
  passwords = [p for p in f.read().split('\n')]

def parseRule(ruleString):
  character = ruleString[-1]
  charmin = int(ruleString[0:ruleString.find('-')])
  charmax = int(ruleString[ruleString.find('-')+1:ruleString.find(':')])

  return (character, list(range(charmin, charmax+1)))


validPWords = 0
for pw in passwords:
  ruleString = pw[:pw.find(':')].strip()
  pword = pw[pw.find(':')+1:].strip()
  
  rule = parseRule(ruleString)

  validPWords += 1 if pword.count(rule[0]) in rule[1] else 0

print(validPWords)