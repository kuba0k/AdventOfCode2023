from itertools import cycle
from math import lcm


def one_star(filename):
    with open(filename) as f:
        lr = cycle(
            list(
                map(
                    lambda x: int(x),
                    f.readline().strip().translate(str.maketrans({"L": "0", "R": "1"})),
                )
            )
        )
        move_map = {}
        for line in f.readlines()[1:]:
            instructions = line.strip().split(" = ")
            move_map[instructions[0]] = (
                instructions[1].removeprefix("(").removesuffix(")").split(", ")
            )

    steps = 0
    position = "AAA"
    while position != "ZZZ":
        position = move_map[position][next(lr)]
        steps += 1
    print(f"Part 1 steps: {steps}")


def two_stars(filename):
    with open(filename) as f:
        lr = cycle(
            list(
                map(
                    lambda x: int(x),
                    f.readline().strip().translate(str.maketrans({"L": "0", "R": "1"})),
                )
            )
        )
        move_map = {}
        for line in f.readlines()[1:]:
            instructions = line.strip().split(" = ")
            move_map[instructions[0]] = (
                instructions[1].removeprefix("(").removesuffix(")").split(", ")
            )
    steps = 0
    positions = list(filter(lambda x: x[-1] == "A", move_map.keys()))
    steps_arr = []

    while positions:
        direction = next(lr)
        steps += 1
        for i in range(len(positions)):
            positions[i] = move_map[positions[i]][direction]
            if positions[i][-1] == "Z":
                steps_arr.append(steps)
        positions = list(filter(lambda x: x[-1] != "Z", positions))

    steps = lcm(*steps_arr)
    print(f"Part 2 steps: {steps}")


# one_star("day8_input.txt")
# two_stars("day8_input.txt")
