from collections import Counter

def read_lists(file_path):
    _list1 = []
    _list2 = []

    with open(file_path, 'r') as f:
        for line in f:
            values = line.split()
            _list1.append(int(values[0]))
            _list2.append(int(values[1]))

    _list2_counter = Counter(_list2)

    return _list1, _list2_counter


list1, list2_counter = read_lists('input/actual.txt')
result = [x * list2_counter[x] for x in list1]
print(sum(result))