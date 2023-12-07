from collections import Counter

type_dict = {
    "[5]": 6,
    "[1, 4]": 5,
    "[2, 3]": 4,
    "[1, 1, 3]": 3,
    "[1, 2, 2]": 2,
    "[1, 1, 1, 2]": 1,
    "[1, 1, 1, 1, 1]": 0,
}

translate_dict = str.maketrans(
    {
        "T": "10",
        "J": "11",
        "Q": "12",
        "K": "13",
        "A": "14",
    }
)
translate_dict_2 = str.maketrans(
    {
        "J": "1",
        "T": "10",
        "Q": "12",
        "K": "13",
        "A": "14",
    }
)


class Hand:
    def __init__(self, hand, bid) -> None:
        self.hand = hand
        self.bid = int(bid)
        self.hand_type_rank = -1
        self.values = None

    def analyse_hand(self):
        # one star
        # 5-five of a kind, 4 four of a kind, ..., 0 high card
        occurences = sorted(list(Counter(self.hand).values()))
        self.hand_type_rank = type_dict[occurences.__str__()]
        self.values = list(
            map(
                lambda x: int(x),
                self.hand.replace("", " ")[1:-1].translate(translate_dict).split(),
            )
        )

    def analyse_hand_with_J(self):
        # two stars
        # 6-five of a kind, 5 four of a kind, ..., 0 high card
        occurences = Counter(self.hand)
        most_common = occurences.most_common()
        if most_common[0][0] == "J":
            most_common = most_common[1][0] if len(most_common) > 1 else "J"
        else:
            most_common = most_common[0][0]
        occurences = sorted(list(Counter(self.hand.replace("J", most_common)).values()))
        self.hand_type_rank = type_dict[occurences.__str__()]
        self.values = list(
            map(
                lambda x: int(x),
                self.hand.replace("", " ")[1:-1].translate(translate_dict_2).split(),
            )
        )


def one_star(filename):
    hands_bids = [line.strip().split() for line in open(filename).readlines()]
    result = 0
    hands = []
    for hand, bid in hands_bids:
        new_hand = Hand(hand, bid)
        new_hand.analyse_hand()
        hands.append(new_hand)
    hands.sort(key=lambda hand: (hand.hand_type_rank, hand.values))
    for bet_value, hand in enumerate(hands, 1):
        result += bet_value * hand.bid
    print(result)


def two_stars(filename):
    hands_bids = [line.strip().split() for line in open(filename).readlines()]
    result = 0
    hands = []
    for hand, bid in hands_bids:
        new_hand = Hand(hand, bid)
        new_hand.analyse_hand_with_J()
        hands.append(new_hand)
    hands.sort(key=lambda hand: (hand.hand_type_rank, hand.values))
    for bid_multiplier, hand in enumerate(hands, 1):
        result += bid_multiplier * hand.bid
    print(result)


# one_star("day7_input.txt")
# two_stars("day7_input.txt")
