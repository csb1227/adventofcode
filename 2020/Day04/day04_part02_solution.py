import numpy as np

passports_input = None
with open('input.txt', 'r') as f:
  passports_input = [p.replace('\n', ' ') for p in f.read().split('\n\n')]

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def byrValidation(x):
  return True if int(x) in list(range(1920, 2003)) else False

def iyrValidation(x):
  return True if int(x) in list(range(2010, 2021)) else False

def eyrValidation(x):
  return True if int(x) in list(range(2020, 2031)) else False

def hgtValidation(x):
  if x[-2:] == 'in' and int(x[0:-2]) in list(range(59,77)):
    return True
  elif x[-2:] == 'cm' and int(x[0:-2]) in list(range(150,194)):
    return True
  else:
    return False

def hclValidation(x):
  try:
    if x[0] == '#' and int(x[1:], 16):
      return True
    else:
      return False
  except:
    return False

def eclValidation(x):
  if x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
    return True
  else:
    return False

def pidValidation(x):  
  try:
    if len(x) == 9 and int(x, 10):
      return True
    else:
      return False
  except:
    return False

fieldValidation = {
  'byr': byrValidation,
  'iyr': iyrValidation,
  'eyr': eyrValidation,
  'hgt': hgtValidation,
  'hcl': hclValidation,
  'ecl': eclValidation,
  'pid': pidValidation
}

passportsInput = []
for p in passports_input:
  s1 = p.split(' ')
  s2 = [s.split(':') for s in s1]
  s3 = {k:v for k,v in s2}
  passportsInput.append(s3)


passportsCheckOne = []
for p in passportsInput:
  presentFields = list(p.keys())
  missingFields = np.setdiff1d(requiredFields, presentFields)
  if len(missingFields) == 0:
    passportsCheckOne.append(p)

passportsCheckTwo = []
for p in passportsCheckOne:
  valid = True
  for k,v in p.items():
    if k =='cid':
      pass
    else:
      valid = valid & fieldValidation[k](v)
  if valid:
    passportsCheckTwo.append(p)

print(len(passportsCheckTwo))



