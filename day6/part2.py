time, distance = open('input.txt').read().splitlines()

duration = int(time.split(':')[1].replace(' ', ''))
record = int(distance.split(':')[1].replace(' ', ''))

product = 1

ways = 0

for speed in range(1, duration):
    if (duration - speed) * speed > record:
        ways += 1

product *= ways
    
print(product)
