from collections import Counter
instructions = None
with open('input.txt', 'r') as f:
  instructions = [i for i in f.read().split('\n')]

oxygen = instructions

for b in range(len(instructions[0])):
    if len(oxygen) != 1:
        print(oxygen)
        oxygenCount = Counter([i[b] for i in oxygen]).most_common(1)[0]
        oxygenMC = oxygenCount[0] if int(oxygenCount[1])*2 > len(oxygen) else '1'
        oxygen = [i for i in oxygen if i[b] == oxygenMC]

co2 = instructions
for b in range(len(instructions[0])):
    if len(co2) != 1:
        print(co2)
        co2Count = Counter([i[b] for i in co2]).most_common(1)[0]
        co2MC = co2Count[0] if int(co2Count[1])*2 > len(co2) else '1'
        co2 = [i for i in co2 if i[b] != co2MC]



    

print(int(oxygen[0], 2))
print(int(co2[0], 2))
print(int(oxygen[0], 2) * int(co2[0], 2))
    