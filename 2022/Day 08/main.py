class Forest(object):
    def __init__(self, trees):
        self.trees = trees
        self._map_trees()
        self._score_visibility()
        self.visible_trees = self._count_visible_trees()
        self.best_tree = self._find_best_tree()

    def _map_trees(self):
        for coords, tree in self.trees.items():
            north = (coords[0]-1, coords[1])
            east = (coords[0], coords[1]+1)
            south = (coords[0]+1, coords[1])
            west = (coords[0], coords[1]-1)
            try:
                tree.north = self.trees[north]
            except KeyError:
                pass
            try:
                tree.east = self.trees[east]
            except KeyError:
                pass
            try:
                tree.south = self.trees[south]
            except KeyError:
                pass
            try:
                tree.west = self.trees[west]
            except KeyError:
                pass

    def _count_visible_trees(self):
        visible_trees = 0

        for _, tree in self.trees.items():
            n_vis = True
            e_vis = True
            s_vis = True
            w_vis = True

            n_tree, e_tree, s_tree, w_tree = tree.north, tree.east, tree.south, tree.west

            while n_tree and n_vis:
                n_vis = True if tree.height > n_tree.height else False
                n_tree = n_tree.north

            while e_tree and e_vis:
                e_vis = True if tree.height > e_tree.height else False
                e_tree = e_tree.east

            while s_tree and s_vis:
                s_vis = True if tree.height > s_tree.height else False
                s_tree = s_tree.south

            while w_tree and w_vis:
                w_vis = True if tree.height > w_tree.height else False
                w_tree = w_tree.west

            visible_trees += 1 if n_vis or e_vis or s_vis or w_vis else 0

        return visible_trees

    def _score_visibility(self):
        for _, tree in self.trees.items():
            n_vis = 0
            e_vis = 0
            s_vis = 0
            w_vis = 0

            n_tree, e_tree, s_tree, w_tree = tree.north, tree.east, tree.south, tree.west

            while n_tree:
                n_vis += 1
                if n_tree.height >= tree.height:
                    break
                n_tree = n_tree.north

            while e_tree:
                e_vis += 1
                if e_tree.height >= tree.height:
                    break
                e_tree = e_tree.east

            while s_tree:
                s_vis += 1
                if s_tree.height >= tree.height:
                    break
                s_tree = s_tree.south

            while w_tree:
                w_vis += 1
                if w_tree.height >= tree.height:
                    break
                w_tree = w_tree.west

            tree.visibility_score = n_vis * e_vis * s_vis * w_vis

    def _find_best_tree(self):
        best_tree = 0
        for _, tree in self.trees.items():
            best_tree = tree.visibility_score if tree.visibility_score > best_tree else best_tree
        return best_tree


class Tree(object):
    def __init__(self, height, coords):
        self.height = int(height)
        self.coords = coords
        self.north = None
        self.east = None
        self.south = None
        self.west = None
        self.visibility_score = 0


def build_forest(f):
    xmax, ymax = len(f), len(f[0])

    trees = {}

    for row in range(xmax):
        for col in range(ymax):
            trees[(row, col)] = Tree(f[row][col], (row, col))

    return Forest(trees)


def open_forest(f):
    with open(f, 'r') as f:
        return [[int(tree) for tree in line] for line in f.read().split('\n')]


if __name__ == '__main__':
    example_input = './input/example_input.txt'
    puzzle_input = './input/puzzle_input.txt'

    forest_raw = open_forest(puzzle_input)
    forest = build_forest(forest_raw)
    print(f'Part 1: {forest.visible_trees}')
    print(f'Part 2: {forest.best_tree}')
