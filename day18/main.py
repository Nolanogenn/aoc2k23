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
            graph[pos] = '#'
    s = len(graph)
    
    x = [x[0] for x in graph]
    y = [x[1] for x in graph]

#    max_x = max(x)
#    min_x = min(x)
#    max_y = max(y)
#    min_y = min(y)
#
#    graph_normalized = {}
#    for node in graph:
#        graph_normalized[(node[0]-min_x, node[1]-min_y)] = graph[node]
#
#    normalized_x = [x[0] for x in graph_normalized]
#    normalized_y = [x[1] for x in graph_normalized]
#    max_x = max(normalized_x)
#    max_y = max(normalized_y)
#
    a = area(y, x)
    A = a+1-s//2
    return A+s

def decode(hexa):
    direction_dict = {
            '0' : 'R',
            '1' : 'D',
            '2' : 'L',
            '3' : 'U'
            }
    meters = int(hexa[2:7],16)
    direction = direction_dict[hexa[-2]]
    return meters, direction

def part2(inputfile):
    pos = (0,0)
    points = [pos]
    s = 0

    for line in inputfile:
        _,_, hexa = line.split()
        meters, direction = decode(hexa)
        d_tuple = dirs[direction]
        pos = (
            pos[0]+d_tuple[0]*meters, pos[1]+d_tuple[1]*meters
            )
        points.append(pos)
        s += meters

    x = [x[0] for x in points]
    y = [x[1] for x in points]
    a = area(x, y)
    A = a+1-s//2
    return A+s

if __name__ == '__main__':
    inputfile = open('day18.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
