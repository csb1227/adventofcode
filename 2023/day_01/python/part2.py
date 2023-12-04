class Part2:
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.numbers_as_words = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

    def solve(self):
        result = []
        calibration_values = self.parse_puzzle_input()
        for cv in calibration_values:
            these_values = []
            first_number = self.find_first_number(cv)
            if first_number is not None:
                these_values.append(first_number)
            last_number = self.find_last_number(cv)
            if last_number is not None:
                these_values.append(last_number)
            first_number_word = self.find_first_number_word(cv)
            if first_number_word is not None:
                these_values.append(first_number_word)
            last_number_word = self.find_last_number_word(cv)
            if last_number_word is not None:
                these_values.append(last_number_word)

            actual_calibration_value = self.evaluate_values(these_values)

            result.append(actual_calibration_value)

        return sum(result)

    @staticmethod
    def evaluate_values(calibration_numbers):
        first_number = None
        last_number = None

        for calibration_number in calibration_numbers:
            first_number = calibration_number if (first_number is None or calibration_number[0] < first_number[0]) else first_number
            last_number = calibration_number if (
                    last_number is None or calibration_number[0] > last_number[0]) else last_number

        return int(first_number[1] + last_number[1])

    def parse_puzzle_input(self):
        with open(self.puzzle_input) as file:
            result = file.read().split("\n")

        return result

    def find_first_number_word(self, calibration_value):
        for i in range(len(calibration_value)):
            for number_word in self.numbers_as_words.keys():
                if str(calibration_value[i:]).startswith(number_word):
                    return i, self.numbers_as_words[number_word]

    def find_last_number_word(self, calibration_value):
        last_i = len(calibration_value)
        for i in range(len(calibration_value)):
            for number_word in self.numbers_as_words.keys():
                if str(calibration_value[last_i - i:]).startswith(number_word):
                    return last_i - i, self.numbers_as_words[number_word]

    @staticmethod
    def find_first_number(calibration_value):
        for character in enumerate(calibration_value):
            try:
                int(character[1])
                return character
            except:
                pass

        return

    @staticmethod
    def find_last_number(calibration_value):
        result = None
        for i in enumerate(calibration_value):
            try:
                result = i if int(i[1]) is not None else int(i)
            except:
                pass

        return result
