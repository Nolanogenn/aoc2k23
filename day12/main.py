import functools

def parsefile(f):
    parsed = []
    for l in f:
        x,y = l.split()
        y = [int(n) for n in y.split(',')]
        parsed.append((x,y)) 
    return parsed

@functools.cache
def check(line, gold, currentcount):
    if len(line) == 0:
        if len(gold) == 0 and currentcount == 0:
            return 1
        elif len(gold) == 1 and currentcount == gold[0]:
            return 1
        else:
            return 0
    if len(gold) > 0 and currentcount > gold[0]:
        return 0
    elif len(gold) == 0 and currentcount > 0:
        return 0

    n = 0
    currentspring = line[0]
    if currentspring in ['#', '?']:
        n += check(line[1:], gold, currentcount+1)
    if currentspring in ['.', '?']:
        if len(gold) > 0 and currentcount == gold[0]:
            n += check(line[1:], gold[1:], 0)
        elif currentcount == 0:
            n += check(line[1:], gold, 0)
    return n
    
def part1(inputfile):
    parsed = parsefile(inputfile)
    arr = []
    for line in parsed:
        springs, tocheck = line
        x = check(springs, tuple(tocheck), 0)
        arr.append(x)
    return sum(arr)

def part2(inputfile):
    parsed = parsefile(inputfile)
    parsed = [
            ('?'.join([line[0]]*5),
            line[1] * 5) for line in parsed
            ]
    arr = []
    for p in parsed:
        line, gold = p
        x = check(line, tuple(gold), 0)
        arr.append(x)
    return sum(arr) 

if __name__ == '__main__':
    inputfile = open('day12.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
