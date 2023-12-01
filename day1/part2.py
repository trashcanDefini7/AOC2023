s = 0

LETTERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input.txt') as f:
    while line := f.readline():
        nums = [0] * 2
        
        while nums[0] == 0:
            if line[0].isdigit():
                nums[0] = int(line[0])
            else:
                for i, l in enumerate(LETTERS):        
                    if line.startswith(l):
                        nums[0] = i + 1
                        break
                
            line = line[1:]
         
        while len(line) > 0 and nums[1] == 0:
            if line[-1].isdigit():
                nums[1] = int(line[-1])
            else:
                for i, l in enumerate(LETTERS):   
                    if line.endswith(l):
                        nums[1] = i + 1
                        break
                
            line = line[:-1]
        
        s += int(''.join([str(nums[((i + 1) % 2) if nums[i] == 0 else i]) for i in (0, 1)]))
        
print(s)
