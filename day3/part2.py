import re
from collections import defaultdict

with open('input.txt') as f:
    s = f.read().splitlines()

adjacent = defaultdict(list)

for i, line in enumerate(s):
    for d in re.finditer(r"\d+", line):
        indices = [(i, d.start() - 1), (i, d.end())]
        indices += [(i - 1, j) for j in range(d.start() - 1, d.end() + 1)]
        indices += [(i + 1, j) for j in range(d.start() - 1, d.end() + 1)]
        
        for a, b in indices:
            if 0 <= a < len(s) and 0 <= b < len(s[a]) and s[a][b] != ".":
                adjacent[a, b].append(d.group())
                
print(sum(int(x[0]) * int(x[1]) for x in adjacent.values() if len(x) == 2))
