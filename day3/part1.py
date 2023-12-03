with open('input.txt') as f:
    s = f.read().splitlines()
    
w = len(s[0])
h = len(s)

res = 0

x, y = 0, 0

while y < h:
    while x < w:
        if s[y][x].isdigit():
            start = x
            x += 1
            
            while x < w and s[y][x].isdigit():
                x += 1
                
            n = int(''.join(s[y][start:x]))
            
            if any([s[j][i] != '.' and not s[j][i].isdigit() for i in range(start - 1, x + 1) for j in range(y - 1, y + 2) if j >= 0 and i >= 0 and i < w and j < h]):
                res += n
                
        x += 1
    
    x = 0
    y += 1
    
print(res)  
    