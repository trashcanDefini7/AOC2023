s = 0

with open('input.txt') as f:
    while line := f.readline():
        numbers = list(filter(lambda c: c.isdigit(), line))
        s += int(numbers[0] + numbers[-1])

print(s)
