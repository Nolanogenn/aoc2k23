def part1(grid):
    graph = {}
    movs = [(0,1), (0,-1), (1,0), (-1,0)]
    max_x = len(grid[0])
    max_y = len(grid)
    starting_pos = [(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 'S'][0]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            graph[(i,j)] = []
            for mov in movs:
                d = (i+mov[0], j+mov[1])
                if d[0] >= 0 and d[0] < max_y and d[1] >= 0 and d[1] < max_x:
                    graph[(i,j)].append((d, grid[d[0]][d[1]]))
          

    v = compute_paths(64, graph, starting_pos)
    return v
def part2(inputfile):
    graph = {}
    movs = [(0,1), (0,-1), (1,0), (-1,0)]
    max_x = len(grid[0])
    max_y = len(grid)
    starting_pos = [(x,y) for x in range(len(grid)) for y in range(len(grid[0])) if grid[x][y] == 'S'][0]
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            graph[(i,j)] = []
            for mov in movs:
                d = (i+mov[0], j+mov[1])
                if d[0] >= 0 and d[0] < max_y and d[1] >= 0 and d[1] < max_x:
                    graph[(i,j)].append((d, grid[d[0]][d[1]]))
          
    num_steps = 26501365
    n = num_steps // max_x
    s = [x*max_x+(max_x//2) for x in range(3)] 
    print(s)
    a,b,c = (compute_paths(y, graph, starting_pos) for y in s)
    v = a + n * (b - a +(n - 1) * (c - b - b + a) // 2)
    return v

def compute_paths(max_steps:int, graph, starting_pos):
    queue = [(starting_pos,0)]
    visited = set()
    count = 0
    while queue:
        tocheck, steps = queue[0]
        queue = queue[1:]
        if tocheck in visited:
            continue
        visited.add(tocheck)
        if steps%2 == max_steps%2: 
            count += 1
        if steps >= max_steps:
            continue
        next_possible_movs = [p[0] for p in graph[tocheck] if p[1] != '#']
        for mov in next_possible_movs:
            queue.append((mov, steps+1))
    return count

if __name__ == '__main__':
    inputfile = open('day21test.txt').readlines()
    grid = [list(x.strip()) for x in inputfile]
    sol1 = part1(grid)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
