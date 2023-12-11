from itertools import combinations

def manhdist(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

def scaledist(universe, rows_to_expand, cols_to_expand, pair, distance, scale):

    range_xs = sorted([p[0] for p in pair])
    range_ys = sorted([p[1] for p in pair])

    rs = len([r for r in rows_to_expand if range_xs[0] < r and range_xs[1] > r])
    cs = len([c for c in cols_to_expand if range_ys[0] < c and range_ys[1] > c])

    distance = distance + ((rs + cs) * scale)
    return distance

def solve(inputfile, scale, rows_to_expand, cols_to_expand):
    v = 0
    scale = scale -1
    for i,p in enumerate(pairs):
        dist = manhdist(p[0], p[1])
        scaled_dist = scaledist(universe,rows_to_expand, cols_to_expand, p, dist, scale)
        v += scaled_dist
    return v


if __name__ == '__main__':
    inputfile = open('day11test.txt').readlines()
    universe = [x.strip() for x in inputfile]
    galaxies = [
            (i,r) for i in range(len(universe)) for r in range(len(universe[i])) if universe[i][r] == '#'
            ]
    rows = list(universe)
    cols = [''.join([r[i] for r in rows]) for i in range(len(rows[0]))]

    rows_to_expand = [i for i,r in enumerate(rows) if all([x == '.' for x in r])]
    cols_to_expand = [i for i,c in enumerate(cols) if all([x == '.' for x in c])]

    pairs = list(combinations(galaxies, 2))
    sol1 = solve(inputfile, 2, rows_to_expand, cols_to_expand)
    print(f"Solution for part 1: {sol1}")

    sol2 = solve(inputfile, 1_000_000, rows_to_expand, cols_to_expand)
    print(f"Solution for part 2: {sol2}")
