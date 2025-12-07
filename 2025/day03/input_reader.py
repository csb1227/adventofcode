def read_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
        return [line.replace("\n", "") for line in lines]