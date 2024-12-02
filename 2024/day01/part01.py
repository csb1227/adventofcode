def read_lists(file_path):
    _list1 = []
    _list2 = []

    with open(file_path, 'r') as f:
        for line in f:
            values = line.split()
            _list1.append(int(values[0]))
            _list2.append(int(values[1]))

    _list1.sort()
    _list2.sort()

    x = list(zip(_list1, _list2))

    return x


list_pairs = read_lists('input/actual.txt')
diffs = [abs(x[0] - x[1]) for x in list_pairs]
print(sum(diffs))