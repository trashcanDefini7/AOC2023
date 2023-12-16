histories = list(map(lambda x: list(map(int, x.split())), open('input.txt').readlines()))

def iterate_until_zeros(data: list[int], output=None) -> list[list[int]]:    
    output = output or [data.copy()]
    out = []
    
    for i in range(len(data) - 1):
        out.append(data[i + 1] - data[i])
    
    if out.count(0) == len(out):
        return output
    
    output.append(out)
    return iterate_until_zeros(out, output)
    

total_sum = 0

for history in histories:
    parts = list(reversed(iterate_until_zeros(history)))
    
    for i in range(1, len(parts)):
        parts[i].append(parts[i][-1] + parts[i-1][-1])
    
    total_sum += parts[-1][-1]

print(total_sum)
