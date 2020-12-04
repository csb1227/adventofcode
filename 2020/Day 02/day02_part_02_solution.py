passwords = None
with open('passwords.txt', 'r') as f:
  passwords = [p for p in f.read().split('\n')]

def parseRule(ruleString):
  character = ruleString[-1]
  charmin = int(ruleString[0:ruleString.find('-')])
  charmax = int(ruleString[ruleString.find('-')+1:ruleString.find(':')])

  return (character, charmin, charmax)

validPWords = 0
for pw in passwords:
  ruleString = pw[:pw.find(':')].strip()
  pword = pw[pw.find(':')+1:].strip()
  
  rule = parseRule(ruleString)

  validPWords += 1 if bool(rule[0] == pword[rule[1]-1]) ^ bool(rule[0] == pword[rule[2]-1]) else 0

print(validPWords)