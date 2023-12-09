import math


data = open('input.txt').read().split('\n\n')

lookup = {key: val[1:-1].split(', ') for key, val in map(lambda x: x.split(' = '), data[1].splitlines()) }

cur_nodes = list(filter(lambda x: x.endswith('A'), lookup.keys()))
cycles = []

for node in cur_nodes:
    cur_steps, step_count = data[0], 0
    
    while step_count == 0 or not node.endswith('Z'):
        step_count += 1
        node = lookup[node][cur_steps[0] == 'R']
        cur_steps = cur_steps[1:] + cur_steps[0]
    
    cycles.append(step_count)
    
print(math.lcm(*cycles))
