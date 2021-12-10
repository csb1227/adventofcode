from collections import Counter

data = [
  [l.split(' ') for l in line.split(' | ')]
  for line in open('input.txt').read().split('\n')
]

segments = {
  2: [1],
  3: [7],
  4: [4],
  5: [2, 3, 5],
  6: [0, 6, 9],
  7: [8]
}

result = 0

for entry in data:
  observations = {}
  revObservations = {}
  five = []
  six = []

  entry[0] = [''.join(sorted(e)) for e in entry[0]]
  entry[1] = [''.join(sorted(e)) for e in entry[1]]

  # add known numbers to observations and split out the rest as 5 or 6 segment entries
  for e in entry[0]:
    if len(e) == 2:
      observations[e] = '1'
      revObservations[1] = e
    elif len(e) == 4:
      observations[e] = '4'
      revObservations[4] = e
    elif len(e) == 3:
      observations[e] = '7'
      revObservations[7] = e
    elif len(e) == 7:
      observations[e] = '8'
      revObservations[8] = e
    elif len(e) == 5:
      five.append(e)
    elif len(e) == 6:
      six.append(e)

  # Five segment numbers

  # among the numbers that have five segments only the 3 has all the 7

  for number in five:
    if all(d in number for d in revObservations[7]):
      observations[number] = '3'
      revObservations[3] = number
      five.remove(number)

  # 2s segments + 4s segments give an 8
  for number in five:
    if len(set(number + revObservations[4])) == 7:
      observations[number] = '2'
      revObservations[2] = number
      five.remove(number)

  # the remaining number in five is 5
  observations[five[0]] = '5'
  revObservations[5] = five[0]
  five.remove(five[0])

  # Six segment numbers ------------------------------------------------------

  # the 9 contains all of the 4
  for number in six:
    if all(d in number for d in revObservations[4]):
      observations[number] = '9'
      revObservations[9] = number
      six.remove(number)

  # the zero contains all of the 1
  for number in six:
    if all(d in number for d in revObservations[1]):
      observations[number] = '0'
      revObservations[0] = number
      six.remove(number)

  # the remaining number in six is 6
  observations[six[0]] = '6'
  revObservations[6] = six[0]
  six.remove(six[0])

  result += int(''.join([observations[e] for e in entry[1]]))
  

print(result)
# (You guessed 1214823. Too high.)