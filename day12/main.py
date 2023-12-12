import functools
from operator import itemgetter
import itertools
import tqdm

def parsefile(f):
    parsed = []
    for l in f:
        x,y = l.split()
        y = [int(n) for n in y.split(',')]
        parsed.append((x,y)) 
    return parsed


def group_consecutives(l):
    l.sort()
    current_elem = l.pop(0)
    current_count = 1
    subl = []
    while l:
        elem = l.pop(0)
        if elem-1 == current_elem:
            current_count +=1
        else:
            subl.append(current_count)
            current_count = 1
        current_elem = elem
    subl.append(current_count)
    return subl

def generate_alts(line, gold):
    idx_present = [i for i,c in enumerate(line) if c == '#']
    idx_substitute = [i for i,c in enumerate(line) if c == '?']

    num_needed = sum(gold) - len(idx_present)
    combinations = itertools.combinations(idx_substitute, num_needed)
    alts = 0
    for combination in combinations:
        tocheck = list(combination)+idx_present
        key = tuple(sorted(tocheck))
        if key in visited:
            continuous = visited[key]
        else:
            continuous = group_consecutives(tocheck)
            visited[key] = continuous
            i = 0
            for j in continuous:
                l = key[i:i+j]
                l = [n-min(l) for n in l]
                visited[tuple(l)] = j
        if continuous == gold:
            alts += 1
    return alts

memory = {}

def section_len(section):
    if all([x == '#' for x in section]):
        return [[len(section)]]
    else:
        x = []
        idx_substitute = [i for i,c in enumerate(section) if c == '?']
        for i in range(len(idx_substitute)):
            combinations = itertools.combinations(idx_substitute, i+1)
            for c in combinations:
                poss = group_consecutives(list(c))
                x.append(poss)
        return x

def check(line):
    l_split = line.split('.')
    toret = []
    for section in l_split:
        toret.append(section_len(section))
    return toret


def part1(inputfile):
    parsed = parsefile(inputfile)
    x = 0
    for p in parsed:
        gold = p[1]
        line = p[0]
        k = check(line)
        combinations = [[elem for y in x for elem in y] for x in itertools.product(*k)]
        n = len([x for x in combinations if x == gold])
        print(line)
        print(combinations, gold)
        x += n
    return x

def part2(inputfile):
    parsed = parsefile(inputfile)
    parsed = [
        ((p[0]+'?')*5, p[1]*5)
        for p in parsed
    ]
    x = 0
    for p in tqdm.tqdm(parsed):
        gold = p[1]
        line = p[0]
        k = check(line, [], 0, line[0], gold)
    return x

if __name__ == '__main__':
    inputfile = open('day12test.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    #sol2 = part2(inputfile)
    #print(f"Solution for part 2: {sol2}")
