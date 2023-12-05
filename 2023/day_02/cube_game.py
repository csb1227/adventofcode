class CubeGame:
    def __init__(self, puzzle_input):
        self.input = puzzle_input
        self.id = None
        self.rounds = self.__parse_input()

    def __repr__(self):
        return "Game {}: {}".format(self.id, ";".join([str(r) for r in self.rounds]))

    def __parse_input(self):
        result = []
        game, raw_rounds = self.input.split(":")
        self.id = int(game.split(" ")[1].strip())
        for raw_round in raw_rounds.split(";"):
            this_round = CubeGameRound()
            for raw_cubes in raw_round.split(","):
                this_round.add(raw_cubes)

            result.append(this_round)

        return result

    def is_valid(self, red, green, blue):
        red_is_valid = all([r.red <= red for r in self.rounds])
        green_is_valid = all([r.green <= green for r in self.rounds])
        blue_is_valid = all([r.blue <= blue for r in self.rounds])

        return red_is_valid and green_is_valid and blue_is_valid

    def fewest_possible_powers(self):
        fewest_reds = max([r.red for r in self.rounds])
        fewest_greens = max([r.green for r in self.rounds])
        fewest_blues = max([r.blue for r in self.rounds])

        return fewest_reds * fewest_greens * fewest_blues


class CubeGameRound:
    def __init__(self):
        self.red = 0
        self.blue = 0
        self.green = 0

    def __repr__(self):
        return "{} blue, {} red, {} green".format(self.blue, self.red, self.green)

    def add(self, cubes):
        number, color = cubes.strip().split(" ")
        self.red += int(number) if color == "red" else 0
        self.blue += int(number) if color == "blue" else 0
        self.green += int(number) if color == "green" else 0

    def is_valid(self, red, green ,blue):
        red_is_valid = True if self.red <= red else False
        green_is_valid = True if self.green <= green else False
        blue_is_valid = True if self.blue <= blue else False

        return red_is_valid and green_is_valid and blue_is_valid
