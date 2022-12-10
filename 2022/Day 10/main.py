
def open_puzzle(r):
    with open(r, 'r') as f:
        return f.read().split('\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    example_input = './input/example.txt'
    puzzle_input = './input/puzzle.txt'

    puzzle = open_puzzle(example_input)
