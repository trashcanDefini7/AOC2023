time, distance = open('input.txt').read().splitlines()

time = list(map(int, time.split()[1:]))
distance = list(map(int, distance.split()[1:]))

product = 1

for duration, record in zip(time, distance):
    ways = 0
    
    for speed in range(1, duration):
        if (duration - speed) * speed > record:
            ways += 1
    
    product *= ways
    
print(product)
