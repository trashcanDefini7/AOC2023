from itertools import cycle

data = open('input.txt').read().split('\n\n')

lookup = {key: val[1:-1].split(', ') for key, val in map(lambda x: x.split(' = '), data[1].splitlines()) }

steps = 0
cur_node = 'AAA'

for step in cycle(data[0]):
    if cur_node == 'ZZZ':
        print(steps)
        break
    
    cur_node = lookup[cur_node][step == 'R']
    steps += 1
