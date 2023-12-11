import pprint
from itertools import combinations

def pad(l):
    pad_to = max([len(x) for x in l])
    padded = []
    for elem in l:
        new_elem = str(elem)
        if len(elem) < pad_to:
            for k in range(pad_to - len(elem)):
                new_elem += '.'
        padded.append(new_elem)

    return padded

def expanduniverse(inputfile):
    rows = [x.strip() for x in inputfile]
    cols = [''.join([r[i] for r in rows]) for i in range(len(rows[0]))]

    len_rows = len(rows[0])
    len_cols = len(cols[0])

    
    empty_row = '.'*len_rows

    rows_to_expand = [i for i,r in enumerate(rows) if all([x == '.' for x in r])]
    cols_to_expand = [i for i,c in enumerate(cols) if all([x == '.' for x in c])]

    new_universe = []
    for r in range(len_rows):
        if r in rows_to_expand:
            new_universe.append(empty_row) 
        new_row = ''
        for c in range(len_cols):
            if c in cols_to_expand: 
                new_row += '.'
            new_row += inputfile[r][c]
        new_universe.append(new_row)
    new_universe = pad(new_universe)
    return new_universe
                                                                      
def getneighbors(graph, node, dist):
    max_c = len(graph[0]) - 1
    max_r = len(graph) - 1

    movs = {
            'up':(-1,0),
            'down':(+1,0),
            'left':(0, -1),
            'right':(0, 1)
            }
    neighbors = []
    for m in movs:
        n = (
                min(max_r, max(0, node[0] + movs[m][0])),
                min(max_c, max(0, node[1] + movs[m][1]))
                )
        neighbors.append((n,dist+1))
    return neighbors

def bfs(universe, source, target):
    tocheck = source
    dist = 0
    n = getneighbors(universe,source,dist)
    visited = set(source)
    while tocheck[0] != target:
        tocheck = n[0]
        if tocheck[0] not in visited:
            visited.add(tocheck[0])
            neighbors = getneighbors(universe,tocheck[0],tocheck[1])
            n.extend([n for n in neighbors if n[0] not in visited])
            n = n[1:]
        else:
            n = n[1:]
    return tocheck[1]

def manhdist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

def part1(inputfile):
    universe = expanduniverse(inputfile)
    galaxies = [
            (i,r) for i in range(len(universe)) for r in range(len(universe[i])) if universe[i][r] == '#'
            ]
    pairs = combinations(galaxies, 2)
    v = 0
    for i,p in enumerate(pairs):
        v += manhdist(p[0], p[1])
    return v

def scaledist(universe, rows_to_expand, cols_to_expand, pair, distance, scale):

    range_xs = sorted([p[0] for p in pair])
    range_ys = sorted([p[1] for p in pair])

    rs = len([r for r in rows_to_expand if range_xs[0] < r and range_xs[1] > r])
    cs = len([c for c in cols_to_expand if range_ys[0] < c and range_ys[1] > c])

    distance = distance + ((rs + cs) * scale)
    return distance

def part2(inputfile):
    universe = [x.strip() for x in inputfile]
    galaxies = [
            (i,r) for i in range(len(universe)) for r in range(len(universe[i])) if universe[i][r] == '#'
            ]
    rows = list(universe)
    cols = [''.join([r[i] for r in rows]) for i in range(len(rows[0]))]

    rows_to_expand = [i for i,r in enumerate(rows) if all([x == '.' for x in r])]
    cols_to_expand = [i for i,c in enumerate(cols) if all([x == '.' for x in c])]
    pairs = list(combinations(galaxies, 2))
    v = 0
    scale = 1_000_000 - 1
    for i,p in enumerate(pairs):
        print(i, end ='\r')
        dist = manhdist(p[0], p[1])
        scaled_dist = scaledist(universe,rows_to_expand, cols_to_expand, p, dist, scale)
        v += scaled_dist
    print(v)
    pass

if __name__ == '__main__':
    inputfile = open('day11test.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
