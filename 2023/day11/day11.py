import re
from functools import reduce


def day11(filename, stars=1):
    image = open(filename).read().split()
    galaxies = []
    empty_rows = 0
    empty_cols = [
        0 if line.find("#") != -1 else 1
        for line in (
            [
                reduce(
                    lambda x, y: x + y, [image[row][col] for row in range(len(image))]
                )
                for col in range(len(image[0]))
            ]
        )
    ]
    for row, line in enumerate(image):
        init_galaxies = [galaxy.span()[0] for galaxy in re.finditer("#", line)]
        if init_galaxies == []:
            empty_rows += 1
        else:
            if stars == 1:
                [galaxies.append((row + empty_rows, col)) for col in init_galaxies]
            else:
                [
                    galaxies.append((row + empty_rows * 999999, col))
                    for col in init_galaxies
                ]
    if stars == 1:
        galaxies = [(row, col + sum(empty_cols[:col])) for (row, col) in galaxies]
    else:
        galaxies = [
            (row, col + sum(empty_cols[:col]) * 999999) for (row, col) in galaxies
        ]
    result = 0
    for i, galaxy in enumerate(galaxies, 1):
        for galaxy2 in galaxies[i:]:
            result += abs(galaxy[0] - galaxy2[0]) + abs(galaxy[1] - galaxy2[1])
    print(f"{stars} star {result=}")


# day11("day11_input.txt", stars=1)
# day11("day11_input.txt", stars=2)
