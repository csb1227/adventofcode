instructions = None
with open('input.txt', 'r') as f:
  instructions = [i for i in f.read().split('\n')]

gamma = ''
epsilon = ''
for b in range(len(instructions[0])):
    bit = 0    
    for i in instructions:
        bit += int(i[b])        
    gamma += '1' if bit*2 > len(instructions) else '0'
    epsilon += '0' if bit*2 > len(instructions) else '1'

print(int(gamma, 2))
print(int(epsilon, 2))
print(int(gamma, 2) * int(epsilon, 2))