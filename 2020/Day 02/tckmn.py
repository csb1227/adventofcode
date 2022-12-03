import re

data = [(lambda a,b,c,d: [int(a), int(b), c, d])(*re.findall(r'\w+', line))
        for line in open('passwords.txt').readlines()]

print(data)

# part 1
print(sum(a <= d.count(c) <= b for a,b,c,d in data))

# part 2
print(sum((d[a-1] == c) != (d[b-1] == c) for a,b,c,d in data))