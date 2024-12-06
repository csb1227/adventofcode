from collections.abc import Set


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        _map = f.read().split('\n')

        return _map


class Guard:
    def __init__(self, guard_map, starting_position, starting_orientation):
        self.initial_map = guard_map
        self.obstacles = self._locate_obstacles()
        self.position = starting_position
        self.orientation = starting_orientation
        self.positions_visited = {starting_position}

    def __repr__(self):
        return f"The guard is at {self.position} facing {self.orientation} and has visited {len(self.positions_visited)} spaces."

    def _locate_obstacles(self):
        obstacles = []
        for row_index, row in enumerate(self.initial_map):
            for column_index, cell in enumerate(row):
                if cell == "#":
                    obstacles.append((row_index, column_index))

        return obstacles

    def view_map(self):
        width = len(self.initial_map[0])
        height = len(self.initial_map)

        current_map = []

        for row in range(height):
            new_row = []
            for col in range(width):
                if (row, col) in self.obstacles:
                    new_row.append("#")
                elif (row, col) in self.positions_visited:
                    new_row.append("X")
                elif (row, col) == self.position:
                    if self.orientation == "N":
                        new_row.append("^")
                    elif self.orientation == "E":
                        new_row.append(">")
                    elif self.orientation == "S":
                        new_row.append("v")
                    elif self.orientation == "W":
                        new_row.append("<")
                else:
                    new_row.append(".")

            current_map.append("".join(new_row))

        return "\n".join(current_map)

    def identify_next_obstacle(self):
        next_obstacle = None

        if self.orientation == "N":
            next_obstacles = [(y, x) for y, x in self.obstacles if y < self.position[0] and x == self.position[1]]
            next_obstacle = sorted(next_obstacles, reverse=True)
        if self.orientation == "E":
            next_obstacles = [(y, x) for y, x in self.obstacles if y == self.position[0] and x > self.position[1]]
            next_obstacle = sorted(next_obstacles)
        if self.orientation == "S":
            next_obstacles = [(y, x) for y, x in self.obstacles if y > self.position[0] and x == self.position[1]]
            next_obstacle = sorted(next_obstacles)
        if self.orientation == "W":
            next_obstacles = [(y, x) for y, x in self.obstacles if y == self.position[0] and x < self.position[1]]
            next_obstacle = sorted(next_obstacles, reverse=True)

        return next_obstacle[0] if next_obstacle else None

    def walk_to(self, position):
        position_delta = (0, 0)
        destination = position

        if self.orientation == "N":
            destination = (position[0] + 1, position[1])
            position_delta = (-1, 0)
        if self.orientation == "E":
            destination = (position[0], position[1] - 1)
            position_delta = (0, 1)
        if self.orientation == "S":
            destination = (position[0] - 1, position[1])
            position_delta = (1, 0)
        if self.orientation == "W":
            destination = (position[0], position[1] + 1)
            position_delta = (0, -1)

        while self.position != destination:
            self.position = tuple(map(sum, zip(self.position, position_delta)))
            self.positions_visited.add(self.position)

    def turn(self):
        if self.orientation == "N":
            self.orientation = "E"
        elif self.orientation == "E":
            self.orientation = "S"
        elif self.orientation == "S":
            self.orientation = "W"
        elif self.orientation == "W":
            self.orientation = "N"

    def end_shift(self):
        if self.orientation == "N":
            while self.position[0] > 0:
                self.position = (self.position[0] - 1, self.position[1])
                self.positions_visited.add(self.position)
        elif self.orientation == "E":
            while self.position[1] < len(self.initial_map[0]):
                self.position = (self.position[0], self.position[1] + 1)
                self.positions_visited.add(self.position)
        elif self.orientation == "S":
            while self.position[0] < len(self.initial_map):
                self.position = (self.position[0] + 1, self.position[1])
                self.positions_visited.add(self.position)
        elif self.orientation == "W":
            while self.position[1] > 0:
                self.position = (self.position[0], self.position[1] - 1)
                self.positions_visited.add(self.position)

        self.positions_visited.remove(self.position)


def get_guard(guard_map: list[str]) -> Guard:
    for row_index, row in enumerate(guard_map):
        for column_index, cell in enumerate(row):
            if cell == "^":
                return Guard(guard_map, (row_index, column_index), "N")


def get_obstacles(guard_map):
    obstacles = []

    for row_index, row in enumerate(guard_map):
        for column_index, cell in enumerate(row):
            if cell == "#":
                obstacles.append((row_index, column_index))

    return obstacles
