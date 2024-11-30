import re

def one_star(input):
    # coded_input = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598..",
    # ]

    coded_input = [line.rstrip("\n") for line in open(input, "r").readlines()]
    
    result = 0
    input_len = len(coded_input)
    line_len = len(coded_input[0])
    sign_search_pattern = re.compile("[^\d.]")

    def check_adjacent(row, col):
        start_idx = col[0]
        end_idx = col[1] - 1
        number_len = end_idx - start_idx + 1
        for i in range(-1, 2, 2):
            current_row = row + i
            if input_len > current_row > -1:
                for j in range(-1, number_len + 1):
                    current_col = start_idx + j
                    if line_len > current_col > -1:
                        if re.match(
                            sign_search_pattern, coded_input[current_row][current_col]
                        ):
                            return True
        if start_idx > 0:
            if re.match(sign_search_pattern, coded_input[row][start_idx - 1]):
                return True
        if end_idx < line_len - 1:
            if re.match(sign_search_pattern, coded_input[row][end_idx + 1]):
                return True

    num_search_pattern = re.compile("\d+")
    for row, line in enumerate(coded_input):
        current_line = [match for match in re.finditer(num_search_pattern, line)]
        if not not current_line:
            for match in current_line:
                if check_adjacent(row, match.span()):
                    result += int(match.group())
    return result


def two_stars(input):
    # coded_input = [
    #     "467..114..",
    #     "...*......",
    #     "..35..633.",
    #     "......#...",
    #     "617*......",
    #     ".....+.58.",
    #     "..592.....",
    #     "......755.",
    #     "...$.*....",
    #     ".664.598..",
    # ]

    coded_input = [line.rstrip("\n") for line in open(input, "r").readlines()]

    result = 0
    input_len = len(coded_input)
    line_len = len(coded_input[0])
    number_search_pattern = re.compile("\d")

    def check_adjacent(row, col):
        start_idx = col[0]
        end_idx = col[1] - 1
        number_len = end_idx - start_idx + 1
        search_indexes = []
        for i in range(-1, 2, 2):
            current_row = row + i
            if input_len > current_row > -1:
                for j in range(-1, number_len + 1):
                    current_col = start_idx + j
                    if line_len > current_col > -1:
                        search_indexes.append((current_row, current_col))

        if start_idx > 0:
            search_indexes.append((row, start_idx - 1))
        if end_idx < line_len - 1:
            search_indexes.append((row, end_idx + 1))

        gears = []
        while len(search_indexes) > 0:
            if len(gears) < 3:
                current_gear = 0
                power = 0
                current_row = search_indexes[0][0]
                current_col = search_indexes[0][1]
                search_indexes.remove((current_row, current_col))
                if re.match(
                    number_search_pattern, coded_input[current_row][current_col]
                ):
                    while current_col < line_len - 1 and re.match(
                        number_search_pattern, coded_input[current_row][current_col + 1]
                    ):
                        current_col += 1

                        if (current_row, current_col) in search_indexes:
                            search_indexes.remove((current_row, current_col))
                    while current_col >= 0 and re.match(
                        number_search_pattern, coded_input[current_row][current_col]
                    ):
                        current_gear += (
                            int(coded_input[current_row][current_col]) * 10**power
                        )
                        power += 1
                        current_col -= 1
                        if (current_row, current_col) in search_indexes:
                            search_indexes.remove((current_row, current_col))
                    gears.append(current_gear)
            else:
                return 0
        if len(gears) == 2:
            return gears[0] * gears[1]
        else:
            return 0

    gear_search_pattern = re.compile("\*")
    for row, line in enumerate(coded_input):
        current_line = [match for match in re.finditer(gear_search_pattern, line)]
        if not not current_line:
            for match in current_line:
                result += check_adjacent(row, match.span())
    return result


# print(one_star("day3_input.txt"))
# print(two_stars("day3_input.txt"))
