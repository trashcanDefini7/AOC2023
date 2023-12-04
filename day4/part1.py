with open('input.txt') as f:
    cards = f.read().splitlines()
    
res = 0
    
for card in cards:
    card = card[card.find(':')+1:]
    
    winning_numbers = list(filter(lambda x: x.isdigit(), card[:card.find('|')-1].split(' ')))
    my_numbers = list(filter(lambda x: x.isdigit(), card[card.find('|')+1:].split(' ')))
    
    first = True
    val = 0
    
    for n in my_numbers:
        if n in winning_numbers:
            if first:
                val = 1
                first = False
            else:
                val *= 2
                
    res += val
        
print(res)
    