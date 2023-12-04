class Part1:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input

    def solve(self):
        calibration_values = self.parse_puzzle_input()
        extracted_numbers = self.extract_numbers(calibration_values)
        calibrations = self.calculate_calibrations(extracted_numbers)

        return sum(calibrations)

    def parse_puzzle_input(self):
        with open(self.puzzle_input) as file:
            result = file.read().split("\n")

        return result

    @staticmethod
    def extract_numbers(calibration_values):
        result = []

        for calibration_value in calibration_values:
            numbers = []
            for character in calibration_value:
                try:
                    numbers.append(int(character))
                except:
                    pass

            result.append(numbers)

        return result

    @staticmethod
    def calculate_calibrations(extracted_numbers):
        result = []

        for number_set in extracted_numbers:
            result.append((number_set[0] * 10) + number_set[-1])

        return result


