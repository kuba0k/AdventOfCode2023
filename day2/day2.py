def one_star(input):
    # coded_input = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    # ]
    coded_input = open(input, "r")
    max_colours = {"red": 12, "green": 13, "blue": 14}
    result = 0
    for line in coded_input:
        possible = True
        line_split = line.replace(",", "").replace(";", "").split()
        for i in range(3, len(line_split), 2):
            if int(line_split[i - 1]) > max_colours[line_split[i]]:
                possible = False
                break
        if possible:
            result += int(line_split[1][:-1])
    return result


def two_stars(input):
    # coded_input = [
    #     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    #     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    #     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    #     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    #     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    # ]
    coded_input = open(input, "r")
    result = 0
    for line in coded_input:
        min_colours = {"red": 0, "green": 0, "blue": 0}
        line_split = line.replace(",", "").replace(";", "").split()
        for i in range(3, len(line_split), 2):
            current_number = int(line_split[i - 1])
            if (
                current_number > min_colours[line_split[i]]
            ):  # min_colours[line_split[i]] == min_colour_number
                min_colours[line_split[i]] = current_number
        result += min_colours["red"] * min_colours["green"] * min_colours["blue"]
    return result


# print(one_star("day2_input.txt"))
print(two_stars("day2_input.txt"))
# test = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# print(test.replace(",", ""))
