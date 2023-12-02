res = 0
i = 1

goal = {'red': 12, 'green': 13, 'blue': 14}

with open('input.txt') as f:
    while line := f.readline():
        for s in [list(map(lambda x: tuple(x[1:].removesuffix('\n').split(' ')), s.split(','))) for s in line[line.find(':')+1:].split(';')]:
            for count, color in s:
                if goal[color] < int(count):
                    print(color, count)
                    break
            else:
                continue
            break
        else:
            res += i
        
        i += 1

print(res)
