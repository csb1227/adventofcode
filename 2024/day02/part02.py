from sample import Sample

def read_samples(file_path):
    with open(file_path, 'r') as f:
        return [Sample([int(x) for x in y.split()]) for y in f.read().split('\n')]

samples = read_samples('input/actual.txt')


print(sum([sample.is_safe_part02() for sample in samples]))
