from collections import Counter
from itertools import product


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
    

alphabet = 'AKQT98765432J'

cards = open('input.txt').read().splitlines()
scores = []

for card in cards:
    hand, bid = card.split()
    strength = calculate_strength(hand)
    
    for comb in product(alphabet[:-1], repeat=hand.count('J')):
        strength = min(strength, calculate_strength(hand.replace('J', '') + ''.join(comb)))
    
    scores.append((strength, [alphabet.index(h) for h in hand], int(bid)))

scores.sort(reverse=True)
print(sum((i + 1) * card[2] for i, card in enumerate(scores)))
