with open('input.txt') as f:
    cards = f.read().splitlines()
    
res = [1] * len(cards)

for i, card in enumerate(cards):
    winning = list(filter(lambda x: x.isdigit(), card[:card.find('|')-1].split(' ')))
    my = list(filter(lambda x: x.isdigit(), card[card.find('|')+1:].split(' ')))
    
    s = len(set(winning).intersection(set(my)))
    
    for j in range(i + 1, i + s + 1):
        res[j] += res[i]
        
print(sum(res))
