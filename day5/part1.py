with open('input.txt') as f:
    seeds, *lookups = f.read().split('\n\n')
    seeds = list(map(int, seeds.split(': ')[1].split(' ')))
    
    for lookup in lookups:
        _, *ranges = lookup.splitlines()
        
        ranges = [list(map(int, r.split())) for r in ranges]
        ranges = [(range(dst, dst + length), range(src, src + length)) for dst, src, length in ranges]
        
        def trans(seed):
            for dst, src in ranges:
                if seed in src:
                    return dst.start + seed - src.start
                
            return seed
        
        seeds = [trans(s) for s in seeds]
        
print(min(seeds))     
