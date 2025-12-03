def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        _map = f.read().split('\n')

        return _map


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # def __lt__(self, other):
    #     return self.x < other.x and self.y < other.y
    #
    # def __gt__(self, other):
    #     return self.x > other.x and self.y > other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def copy(self):
        return Position(self.x, self.y)

    def go_north(self):
        self.y -= 1

    def go_south(self):
        self.y += 1

    def go_east(self):
        self.x += 1

    def go_west(self):
        self.x -= 1

    def as_tuple(self) -> (int, int):
        return self.y, self.x

    def one_north(self):
        return Position(self.x, self.y - 1)

    def one_south(self):
        return Position(self.x, self.y + 1)

    def one_east(self):
        return Position(self.x + 1, self.y)

    def one_west(self):
        return Position(self.x - 1, self.y)

    def look_left(self, orientation):
        if orientation == "N":
            return self.one_west()
        if orientation == "E":
            return self.one_north()
        if orientation == "S":
            return self.one_west()
        if orientation == "W":
            return self.one_south()

    def all_points_between(self, other):
        points = []

        if self.x == other.x:
            if self.y < other.y:
                for y in range(self.y, other.y + 1):
                    points.append(Position(self.x, y))
            else:
                for y in range(other.y, self.y + 1):
                    points.append(Position(self.x, y))
        elif self.y == other.y:
            if self.x < other.x:
                for x in range(self.x, other.x + 1):
                    points.append(Position(x, self.y))
            else:
                for x in range(other.x, self.x + 1):
                    points.append(Position(x, self.y))

        return points


class Guard:
    def __init__(self, guard_map, starting_position, starting_orientation):
        self.initial_map = guard_map

        self.obstacles: list[Position] = self._locate_obstacles()
        self.frustrating_obstacles = []

        self.position = Position(starting_position[1], starting_position[0])
        self.orientation = starting_orientation
        self.positions_visited = {self.position.copy()}

        self.northbound_routes = []
        self.eastbound_routes = []
        self.southbound_routes = []
        self.westbound_routes = []

        self.current_map = self.view_map()

    def __repr__(self):
        return f"The guard is at {self.position} facing {self.orientation} and has visited {len(self.positions_visited)} spaces."

    def _locate_obstacles(self) -> list[Position]:
        obstacles = []
        for row_index, row in enumerate(self.initial_map):
            for column_index, cell in enumerate(row):
                if cell == "#":
                    obstacles.append(Position(column_index, row_index))

        return obstacles

    def return_path(self):
        if self.orientation in ["N", "S"]:
            left_most = self.position.copy()
            right_most = self.position.copy()

            try:
                while self.initial_map[self.position.y][left_most.x] == ".":
                    left_most.go_west()
            except IndexError:
                pass
            finally:
                left_most.go_east()

            try:
                while self.initial_map[self.position.y][right_most.x] == ".":
                    right_most.go_east()
            except IndexError:
                pass
            finally:
                right_most.go_west()

            return left_most.all_points_between(right_most)

        if self.orientation in ["E", "W"]:
            top_most = self.position.copy()
            bottom_most = self.position.copy()

            try:
                while self.initial_map[top_most.y][self.position.x] == ".":
                    top_most.go_north()
            except IndexError:
                pass
            finally:
                top_most.go_south()

            try:
                while self.initial_map[bottom_most.y][self.position.x] == ".":
                    bottom_most.go_south()
            except IndexError:
                pass
            finally:
                bottom_most.go_north()

            return top_most.all_points_between(bottom_most)

    def look_left(self):
        return self.position.look_left(self.orientation)

    def view_map(self):
        width = len(self.initial_map[0])
        height = len(self.initial_map)

        current_map = []

        for row in range(height):
            new_row = []
            for col in range(width):
                if Position(col, row) in self.obstacles:
                    new_row.append("#")
                elif Position(col, row) in self.northbound_routes or Position(col, row) in self.southbound_routes:
                    new_row.append("|")
                elif Position(col, row) in self.eastbound_routes or Position(col, row) in self.westbound_routes:
                    new_row.append("-")
                elif Position(col, row) in self.positions_visited and Position(col, row) != self.position:
                    new_row.append("X")
                elif Position(col, row) == self.position:
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

    def next_obstacle_ahead(self):
        next_obstacle = None

        if self.orientation == "N":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y < self.position.y and obstacle.x == self.position.x]
            next_obstacle = sorted(next_obstacles, key=lambda p: p.y, reverse=True)
        if self.orientation == "E":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y == self.position.y and obstacle.x > self.position.x]
            next_obstacle = sorted(next_obstacles, key=lambda p: p.x)
        if self.orientation == "S":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y > self.position.y and obstacle.x == self.position.x]
            next_obstacle = sorted(next_obstacles, key=lambda p: p.y)
        if self.orientation == "W":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y == self.position.y and obstacle.x < self.position.x]
            next_obstacle = sorted(next_obstacles, key=lambda p: p.x, reverse=True)

        return next_obstacle[0] if next_obstacle else None

    def next_obstacle_behind(self):
        next_obstacle = None

        if self.orientation == "N":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y > self.position.y and obstacle.x == self.position.x]
            if len(next_obstacles) == 0:
                next_obstacle = Position(self.position.x, len(self.initial_map) - 1)
            else:
                next_obstacle = sorted(next_obstacles, key=lambda p: p.y)[0]
        if self.orientation == "E":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y == self.position.y and obstacle.x < self.position.x]
            if len(next_obstacles) == 0:
                next_obstacle = Position(0, self.position.y)
            else:
                next_obstacle = sorted(next_obstacles, key=lambda p: p.x, reverse=True)[0]
        if self.orientation == "S":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y < self.position.y and obstacle.x == self.position.x]
            if len(next_obstacles) == 0:
                next_obstacle = Position(self.position.x, 0)
            else:
                next_obstacle = sorted(next_obstacles, key=lambda p: p.y, reverse=True)[0]
        if self.orientation == "W":
            next_obstacles = [Position(obstacle.x, obstacle.y) for obstacle in self.obstacles if
                              obstacle.y == self.position.y and obstacle.x > self.position.x]
            if len(next_obstacles) == 0:
                next_obstacle = Position(len(self.initial_map[0]) - 1, self.position.y)
            else:
                next_obstacle = sorted(next_obstacles, key=lambda p: p.x)[0]

        return next_obstacle

    def walk_to(self, position):
        destination = position
        take_a_step = None

        if self.orientation == "N":
            destination = position.one_south()
            take_a_step = self.position.go_north
        if self.orientation == "E":
            destination = position.one_west()
            take_a_step = self.position.go_east
        if self.orientation == "S":
            destination = position.one_north()
            take_a_step = self.position.go_south
        if self.orientation == "W":
            destination = position.one_east()
            take_a_step = self.position.go_west

        obstacle_behind_me = self.next_obstacle_behind()

        all_points_between = obstacle_behind_me.all_points_between(destination)

        if self.orientation == "N":
            [self.northbound_routes.append(p) for p in all_points_between]
        if self.orientation == "E":
            [self.eastbound_routes.append(p) for p in all_points_between]
        if self.orientation == "S":
            [self.southbound_routes.append(p) for p in all_points_between]
        if self.orientation == "W":
            [self.westbound_routes.append(p) for p in all_points_between]

        while self.position != destination:
            if self.position.look_left(self.orientation) in self.obstacles:
                if self.orientation == "N":
                    [self.northbound_routes.append(p) for p in self.return_path()]
                if self.orientation == "E":
                    [self.eastbound_routes.append(p) for p in self.return_path()]
                if self.orientation == "S":
                    [self.southbound_routes.append(p) for p in self.return_path()]
                if self.orientation == "W":
                    [self.westbound_routes.append(p) for p in self.return_path()]

            if self.orientation == "N" and self.position in self.eastbound_routes:
                self.frustrating_obstacles.append(self.position.one_north())
            elif self.orientation == "E" and self.position in self.southbound_routes:
                self.frustrating_obstacles.append(self.position.one_east())
            elif self.orientation == "S" and self.position in self.westbound_routes:
                self.frustrating_obstacles.append(self.position.one_south())
            elif self.orientation == "W" and self.position in self.northbound_routes:
                self.frustrating_obstacles.append(self.position.one_west())

            take_a_step()

            self.positions_visited.add(self.position.copy())

            # self.current_map = self.view_map()
            # print(self.current_map)
            # print("\n")

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
            self.walk_to(Position(self.position.x, 0).one_north())
        elif self.orientation == "E":
            self.walk_to(Position(len(self.initial_map[0]), self.position.y).one_east())
        elif self.orientation == "S":
            self.walk_to(Position(self.position.x, len(self.initial_map)).one_south())
        elif self.orientation == "W":
            self.walk_to(Position(0, self.position.y).one_west())

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
                obstacles.append(Position(column_index, row_index))

    return obstacles
