import numpy as np
from word2number import w2n


def day1_f(filename):
    result = 0
    coded_coordinates = open(filename, "r")
    # coded_coordinates = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    for line in coded_coordinates:
        for el in line:
            if 47 < ord(el) < 58:
                first = int(el)
                break
        for el in reversed(line):
            if 47 < ord(el) < 58:
                last = int(el)
                break
        result += first * 10 + last
    return result


def day1_f_2star(filename):
    numbers_str = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
    ]
    result = 0
    coded_coordinates = open(filename, "r")
    # coded_coordinates = [
    #     "two1nine",
    #     "eightwothree",
    #     "abcone2threexyz",
    #     "xtwone3four",
    #     "4nineeightseven2",
    #     "zoneight234",
    #     "7pqrstsixteen",
    # ]
    for line in coded_coordinates:
        line_length = len(line)
        start_idx = 0
        end_idx = 1
        first = None
        last = None
        while start_idx < line_length:
            while end_idx <= line_length:
                if line[start_idx:end_idx] in numbers_str:
                    first = w2n.word_to_num(line[start_idx:end_idx])
                    break
                end_idx += 1
            if first is not None:
                break
            start_idx += 1
            end_idx = start_idx + 1

        end_idx = line_length
        start_idx = line_length - 1
        while end_idx >= 1:
            while start_idx >= 0:
                if line[start_idx:end_idx] in numbers_str:
                    last = w2n.word_to_num(line[start_idx:end_idx])
                    break
                start_idx -= 1
            if last is not None:
                break
            end_idx -= 1
            start_idx = end_idx - 1
        result += 10 * first + last
    return result


# print(day1_f("day1_input.txt"))
# print(day1_f_2star("day1_input.txt"))
