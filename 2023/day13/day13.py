from functools import reduce


def one_star(filename):
    lines = open(filename).readlines()
    patterns = []
    i = 0
    for line in lines:
        if line != "\n":
            if len(patterns) == i:
                patterns.append([])
            patterns[i].append(line.strip())
        else:
            i += 1

    pattern_cols = [
        [
            [pattern[row][col] for row in range(len(pattern))]
            for col in range(len(pattern[0]))
        ]
        for pattern in patterns
    ]

    def find_mirror(pattern, pattern_cols):
        pat_len = len(pattern) - 1
        pat_col_len = len(pattern_cols) - 1
        for i in range(1, pat_len):  # up
            if pattern[:i] == pattern[i * 2 - 1 : i - 1 : -1]:
                return i * 100
        for i in range(-2, -pat_len, -1):  # down
            if pattern[-1:i:-1] == pattern[i : i * 2 + 1 : -1][::-1]:
                return (len(pattern) + i + 1) * 100
        for i in range(1, pat_col_len):  # left
            if pattern_cols[:i] == pattern_cols[i : i * 2 : 1][::-1]:
                return i
        for i in range(-2, -pat_col_len, -1):  # right
            if pattern_cols[-1:i:-1] == pattern_cols[i : i * 2 + 1 : -1][::-1]:
                return len(pattern_cols) + i + 1

    def check_diff(pat1, pat2):
        diff = 0
        differences = []
        for row, row2 in zip(pat1, pat2):
            diff = 0
            for char1, char2 in zip(row, row2):
                diff = diff if char1 == char2 else diff + 1
            if diff > 1:
                return False
            differences.append(diff)
        return True if reduce(lambda x, y: x + y, differences) == 1 else False

    def find_mirror2(pattern, pattern_cols):
        pat_len = len(pattern) - 1
        pat_col_len = len(pattern_cols) - 1
        for i in range(1, pat_len):  # up
            if check_diff(pattern[:i], pattern[i * 2 - 1 : i - 1 : -1]):
                return i * 100
        for i in range(-2, -pat_len, -1):  # down
            if check_diff(pattern[-1:i:-1], pattern[i : i * 2 + 1 : -1][::-1]):
                return (len(pattern) + i + 1) * 100
        for i in range(1, pat_col_len):  # left
            if check_diff(pattern_cols[:i], pattern_cols[i : i * 2 : 1][::-1]):
                return i
        for i in range(-2, -pat_col_len, -1):  # right
            if check_diff(
                pattern_cols[-1:i:-1], pattern_cols[i : i * 2 + 1 : -1][::-1]
            ):
                return len(pattern_cols) + i + 1

    result1 = 0
    result2 = 0
    for pat_rows, pat_cols in zip(patterns, pattern_cols):
        result1 += find_mirror(pat_rows, pat_cols)
        result2 += find_mirror2(pat_rows, pat_cols)
    print(f"Result part 1: {result1}")
    print(f"Result part 2: {result2}")


one_star("day13_input.txt")
