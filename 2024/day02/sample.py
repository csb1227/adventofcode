class Sample:
    def __init__(self, readings):
        self.readings: list[int] = readings
        self.adjacent_pairs: list[tuple[int, int]] = [(self.readings[i], self.readings[i + 1]) for i in range(len(self.readings) - 1)]
        self.reading_variations: list[int] = [int(x) - int(y) for x, y in self.adjacent_pairs]

    def __repr__(self):
        return ' '.join(self.readings)

    def is_safe_part01(self) -> bool:
        return self._safe_ascent(self.reading_variations) or self._safe_descent(self.reading_variations)

    @staticmethod
    def _safe_ascent(variations) -> bool:
        return all(0 < x <= 3 for x in variations)

    @staticmethod
    def _safe_descent(variations) -> bool:
        return all(-3 <= x < 0 for x in variations)

    def is_safe_part02(self) -> bool:
        if self._safe_ascent(self.reading_variations) or self._safe_descent(self.reading_variations):
            return True

        for i in range(len(self.reading_variations) + 1):
            _modified_list = self.readings[:i] + self.readings[i + 1:]
            _modified_adjacent_pairs = [(_modified_list[i], _modified_list[i + 1]) for i in
                                        range(len(_modified_list) - 1)]
            _modified_variations = [x - y for x, y in _modified_adjacent_pairs]

            if self._safe_ascent(_modified_variations) or self._safe_descent(_modified_variations):
                return True

        return False
