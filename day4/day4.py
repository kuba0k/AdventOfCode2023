from collections import defaultdict

coded_input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]


def one_star(filename):
    coded_input = open(filename, "r").read().split("\n")
    result = 0
    for line in coded_input:
        matching = -1
        [winning, elfs] = [numbers.split() for numbers in line.split(":")[1].split("|")]
        for number in winning:
            if number in elfs:
                matching += 1
        result += 2**matching if matching != -1 else 0
    return result


def two_stars(filename):
    coded_input = open(filename, "r").read().split("\n")
    result = 0
    cards_added = defaultdict(lambda: 1)
    for card_number, line in enumerate(coded_input):
        matching = 0
        [winning, elfs] = [numbers.split() for numbers in line.split(":")[1].split("|")]
        for number in winning:
            if number in elfs:
                matching += 1
        for _ in range(cards_added[card_number]):
            result += 1
            for i in range(1, matching + 1):
                cards_added[card_number + i] += 1
    return result


def two_stars(filename):
    coded_input = open(filename, "r").read().split("\n")
    cards_added = defaultdict(lambda: 1)
    for card_number, line in enumerate(coded_input):
        cards_added[card_number] += 0
        matching = 1
        [winning, elfs] = [numbers.split() for numbers in line.split(":")[1].split("|")]
        for number in winning:
            if number in elfs:
                cards_added[card_number + matching] += cards_added[card_number]
                matching += 1
    return sum(cards_added.values())


# print(one_star("day4_input.txt"))
# print(two_stars("day4_input.txt"))
