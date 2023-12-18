import numpy as np

dirs = {
    'R' : (0, 1),
    'D' : (1, 0),
    'L' : (0, -1),
    'U' : (-1, 0)
}

def area(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

def part1(inputfile):
    graph = {}
    pos = (0,0)
    graph[pos] = '#'
    for line in inputfile:
        d, m, _ = line.split()
        d_tuple = dirs[d]
        for j in range(int(m)):
            pos = (
                pos[0]+d_tuple[0], pos[1]+d_tuple[1]
                )
            print(pos, d_tuple)
            graph[pos] = '#'
    print(graph) 
    s = len(graph)
    
    x = [x[0] for x in graph]
    y = [x[1] for x in graph]
    max_x = max(x)
    min_x = min(x)
    max_y = max(y)
    min_y = min(y)

    graph_normalized = {}
    for node in graph:
        graph_normalized[(node[0]-min_x, node[1]-min_y)] = graph[node]

    normalized_x = [x[0] for x in graph_normalized]
    normalized_y = [x[1] for x in graph_normalized]
    max_x = max(normalized_x)
    max_y = max(normalized_y)

    map = [['.' for _ in range(max_y+1)] for _ in range(max_x+1)]
    for node in graph_normalized:
        map[node[0]][node[1]] = '#'

    map = '\n'.join([''.join(x) for x in map])
    #print(map)
    
    a = area(graph)
    return a

def part2(inputfile):
    pass

if __name__ == '__main__':
    inputfile = open('day18test.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
