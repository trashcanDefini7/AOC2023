res = 0

with open('input.txt') as f:
    while line := f.readline():
        maxs = { 'red': 0, 'green': 0, 'blue': 0 }
        for s in [list(map(lambda x: tuple(x[1:].removesuffix('\n').split(' ')), s.split(','))) for s in line[line.find(':')+1:].split(';')]:
            for count, color in s:
                maxs[color] = max(maxs[color], int(count))
                
        res += maxs['red'] * maxs['green'] * maxs['blue']

print(res)
