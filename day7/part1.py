from collections import Counter


def calculate_strength(hand: str):
    match [count for _, count in Counter(hand).most_common()]:
        case 5, *_:
            return 0
        case 4, *_:
            return 1
        case 3, 2, *_:
            return 2
        case 3, *_:
            return 3
        case 2, 2, *_:
            return 4
        case 2, *_:
            return 5
        case _:
            return 6
    

alphabet = 'AKQJT98765432'

cards = open('input.txt').read().splitlines()
scores = []

for card in cards:
    hand, bid = card.split()
    scores.append((calculate_strength(hand), [alphabet.index(h) for h in hand], int(bid)))

scores.sort(reverse=True)
print(sum((i + 1) * card[2] for i, card in enumerate(scores)))
