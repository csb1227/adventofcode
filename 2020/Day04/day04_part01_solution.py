import numpy as np

passports_input = None
with open('input.txt', 'r') as f:
  passports_input = [p.replace('\n', ' ') for p in f.read().split('\n\n')]

requiredFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


passports = []
for p in passports_input:
  s1 = p.split(' ')
  s2 = [s.split(':') for s in s1]
  s3 = {k:v for k,v in s2}
  passports.append(s3)

validCount = 0
for p in passports:
  presentFields = list(p.keys())
  missingFields = np.setdiff1d(requiredFields, presentFields)
  if len(missingFields) == 0:
    validCount += 1


print(validCount)
