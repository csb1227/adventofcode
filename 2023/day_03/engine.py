class Engine:
    def __init__(self, schematic):
        self.schematic = schematic
        self.part_indicators = self.find_part_indicators()

    def __repr__(self):
        return "\n".join(self.schematic)

    def find_part_indicators(self):
        result = []

        for y in range(len(self.schematic)):
            for x in range(len(self.schematic[y])):
                if self.is_part_indicator(self.schematic[y][x]):
                    result.append((y, x))

        return result

    def find_possible_part_numbers(self):
        result = []

        for y in range(len(self.schematic)):
            asdf = []
            part_number = ""
            part_coords = []
            for x in range(len(self.schematic[y])):
                if self.is_int(self.schematic[y][x]):
                    part_number += self.schematic[y][x]
                    part_coords.append((y, x))
                else:
                    if part_number != "":
                        result.append((part_number, part_coords))
                        part_number = ""
                        part_coords = []

            # result.append(asdf)

        return result

    def identify_engine_parts(self, possible_parts):
        result = []

        for possible_part in possible_parts:
            x = [self.is_adjacent_to_part_indicator(part_coord) for part_coord in possible_part[1]]
            if any(x):
                result.append(int(possible_part[0]))
                print(int(possible_part[0]))

        return result

    def is_adjacent_to_part_indicator(self, part_coord):
        positions_to_check = [
            (part_coord[0] - 1, part_coord[1] - 1),
            (part_coord[0] - 1, part_coord[1]),
            (part_coord[0] - 1, part_coord[1] + 1),
            (part_coord[0], part_coord[1] - 1),
            (part_coord[0], part_coord[1] + 1),
            (part_coord[0] + 1, part_coord[1] - 1),
            (part_coord[0] + 1, part_coord[1]),
            (part_coord[0] + 1, part_coord[1] + 1)
        ]

        if any([position_to_check for position_to_check in positions_to_check if position_to_check in self.part_indicators]):
            return True

        return False

    def is_part_indicator(self, schematic_character):
        return schematic_character != "." and not self.is_int(schematic_character)

    @staticmethod
    def is_int(value):
        try:
            int(value)
            return True
        except:
            return False
