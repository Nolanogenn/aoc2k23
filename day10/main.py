import pprint
def get_connections(tile,tiles,coords):
    movs = tiles[tile]
    toret = []
    for mov in movs:
        coord = (
                max(coords[0]+mov[0],0),
                max(coords[1]+mov[1],0)
            )
        toret.append(coord)
    return toret

def parsing(f):
    tiles = {
            '|' : [(-1, 0), (1, 0)],
            '-' : [(0, -1), (+0, +1)],
            'L' : [(-1, 0), (+0, 1)],
            'J' : [(0, -1), (-1, 0)],
            '7' : [(0, -1), (1, +0)],
            'F' : [(1, +0), (+0, 1)],
            }
    graph = {}
    for x, row in enumerate(f):
        for y, col in enumerate(row):
            if col in tiles:
                conns = get_connections(col, tiles, (x,y))
                graph[(x,y)] = conns
            elif col == 'S':
                s_coords = (x,y)
    graph[s_coords] = [x for x in graph if s_coords in graph[x]]
    return graph, s_coords

def parsing2(f):
    tiles = {
            '|' : [(-1, 0), (1, 0)],
            '-' : [(0, -1), (+0, +1)],
            'L' : [(-1, 0), (+0, 1)],
            'J' : [(0, -1), (-1, 0)],
            '7' : [(0, -1), (1, +0)],
            'F' : [(1, +0), (+0, 1)],
            '.' : [(1,0), (0,1), (-1, 0), (0,-1)]
            }
    graph = {}
    for x, row in enumerate(f):
        for y, col in enumerate(row):
            if col in tiles:
                conns = get_connections(col, tiles, (x,y))
                graph[(x,y)] = conns
            elif col == 'S':
                s_coords = (x,y)
    graph[s_coords] = [x for x in graph if s_coords in graph[x]]
    return graph, s_coords
def bst(graph, coord):
    dists = {}
    dists[coord] = 0
    visited = set()
    v = [coord[0], coord[1], 0]
    tovisit = [v]
    while len(tovisit) > 0:
        v = tovisit[0]
        visited.add((v[0], v[1]))
        dists[(v[0], v[1])] = v[2]
        new_coords = graph[(v[0], v[1])]
        dist = v[2] + 1
        for coord in new_coords:
            new_coord = [coord[0], coord[1], dist]
            if (new_coord[0], new_coord[1]) not in visited:
                tovisit.append(new_coord)
        tovisit = tovisit[1:]
    return dists

def part1(inputfile):
    graph, starting_coord = parsing(inputfile)
    dists = bst(graph, starting_coord)
    max_dist = [v for x,v in sorted(dists.items(), key=lambda x:x[1], reverse=True)][0]
    return max_dist

def check_squeeze(graph, coord):
    movs_tile = {
            #(0,1) : '-.J#',
            (0,1) : '.#',
            (1,0) : '|LJ.#',
            #(0,-1) : '-.#',
            (0,-1) : '.#',
            (-1, 0) : '|LJ.#'
            }
    max_row = max([x[0] for x in graph])
    max_col = max([x[1] for x in graph])
    neighbors = {x :
            (
                min(
                    max(coord[0]+x[0],0),
                    max_row
                    ),
                min(
                    max(coord[1]+x[1],0),
                    max_col
                    )
            )
            for x in movs_tile
                 }
    neighbors_good = [
            neighbors[x] 
            for x in neighbors 
            if graph[neighbors[x]] 
            in movs_tile[x]
            and graph[coord]
            in movs_tile[x]
            ]
    return neighbors_good

def visualize(graph, row, cols):
    toprint = ''
    for i in range(row):
        line = ''
        for k in range(cols):
            line += graph[(i,k)]
        line += '\n'
        toprint += line
    return toprint

def part2(inputfile):
    #movs_tiles = {
    #        '|' : [(-1, 0), (1, 0)],
    #        '-' : [(0, -1), (+0, +1)],
    #        'L' : [(-1, 0), (+0, 1)],
    #        'J' : [(0, -1), (-1, 0)],
    #        '7' : [(0, -1), (1, +0)],
    #        'F' : [(1, +0), (+0, 1)],
    #        '.' : [(1,0), (0,1), (-1, 0), (0,-1)]
    #        }
    #graph, starting_coord = parsing(inputfile)
    #main_loop = list(bst(graph, starting_coord))
    #tiles = {
    #        (x,y) : col
    #        if (x,y) in main_loop
    #        else '.'
    #        for x,row in enumerate(inputfile)
    #        for y,col in enumerate(row.replace('\n', ''))
    #        }
    #orig_tiles = dict(tiles)
    #len_tiles = len(tiles)
    #len_loop = len(main_loop)

    #mov_to_starting = [(x[0]-starting_coord[0],x[1]-starting_coord[1]) for x in graph[starting_coord]]
    #mov = [m for m in movs_tiles if all([x in movs_tiles[m] for x in mov_to_starting])][0]

    #tiles[starting_coord] = mov
    #max_row = max([x[0] for x in tiles])+1
    #max_col = max([x[1] for x in tiles])+1

    #outside_tiles = sorted([
    #        t for t in tiles if tiles[t] == '.'
    #        and (
    #            (0 in t)
    #            or 
    #            (t[0] == max_row-1)
    #            or
    #            (t[1] == max_col-1)
    #            )
    #            ])
    #num_outside = len(outside_tiles)
    #tocheck = outside_tiles
    #for t in outside_tiles:
    #    tiles[t] = '#'
    #visited = set(outside_tiles + tocheck)
    #while len(tocheck)>0:
    #    print(num_outside, end='\r')
    #    check = tocheck[0]
    #    visited.add(check)
    #    additional_tiles = list(set([
    #                    x for x in check_squeeze(tiles, check)
    #                    if x not in visited and x not in tocheck
    #                    ]))
    #    o_t = [x for x in additional_tiles if tiles[x] == '.']
    #    for t in o_t:
    #        tiles[t] = '#'
    #    outside_tiles.extend(o_t)
    #    to_add = len(o_t)
    #    num_outside += to_add
    #    tocheck.extend(additional_tiles)
    #    tocheck = tocheck[1:]

    #viz = visualize(tiles, max_row, max_col)
    #print(viz)
    #return (len_tiles - num_outside - len_loop)
    #coords = N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
    #d = {'|': (N, S), '-': (E, W), 'L': (N, E), 'J': (N, W), '7': (S, W), 'F': (S, E), '.': ()}

    #x, y = next(((i, j) for i, s in enumerate(inputfile) for j, ch in enumerate(s) if ch == "S"), None)
    #q = [((x-dx, y-dy), 1) for dx, dy in coords if (dx, dy) in d[inputfile[x-dx][y-dy]]]
    #visited = {(x, y)}.union(elem[0] for elem in q)

    #while q:
    #    (x,y), graph = q.pop(0)
    #    for (dx, dy) in d[inputfile[x][y]]:
    #        n = (x + dx, y + dy)
    #        if n not in visited:
    #            q.append((n, graph + 1))
    #            visited.add(n)

    #val = 0

    #for i in range(len(inputfile)):
    #    above = False
    #    for j in range(len(inputfile[i])):
    #        if inputfile[i][j] in {'|','L','J'} and (i,j) in visited: above = not above
    #        if above and (i,j) not in visited: val += 1
    #return val

if __name__ == '__main__':
    #inputfile = open('day10.txt').read().strip().splitlines()
    inputfile = open('day10.txt').readlines()
    #sol1 = part1(inputfile)
    #print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
