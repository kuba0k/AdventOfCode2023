from numpy import array
from functools import reduce


def one_star(filename):
    sequences = [
        array(list(map(lambda x: int(x), line.split())))
        for line in open(filename).read().split("\n")
    ]
    result = 0
    for seq in sequences:
        prev_sequences = []
        while not all(seq == 0):
            prev_sequences.append(seq)
            seq = seq[1:] - seq[:-1]
        result += reduce(
            lambda x, y: x[-1] if isinstance(x, int) else x + y[-1], prev_sequences
        )[-1]
    print(f"Part 1 result: {result}")


def two_stars(filename):
    sequences = [
        array(list(map(lambda x: int(x), line.split())))
        for line in open(filename).read().split("\n")
    ]
    result = 0
    for seq in sequences:
        prev_sequences = []
        while not all(seq == 0):
            prev_sequences.append(seq)
            seq = seq[1:] - seq[:-1]
        prev_sequences.append(seq)
        result += reduce(
            lambda x, y: y - x[0] if isinstance(y, int) else y[0] - x,
            reversed(prev_sequences),
        )[-1]

    print(f"Part 2 result: {result}")


# one_star("day9_input.txt")
# two_stars("day9_input.txt")
