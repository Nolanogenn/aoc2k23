def parser(inputfile):
    movs = inputfile[0].strip()
    parsedgraph = [x.replace('\n', '').split('=') for x in inputfile[2:]]
    nodes = [x[0].replace(' ','') for x in parsedgraph]
    links = [x[1].replace('(', '').replace(')', '').split(',') for x in parsedgraph]
    graph = {
            nodes[i] : {
                'L' : links[i][0].replace(' ',''),
                'R' : links[i][1].replace(' ','')
                }
            for i in range(len(nodes))
            }
    return movs, graph

def part1(inputfile):
    movs, graph = parser(inputfile)
    node = 'AAA'
    mov_i = 0
    num_mov = 0
    while node != 'ZZZ':
        if mov_i >= len(movs):
            mov_i = 0
        mov = movs[mov_i]
        node = graph[node][mov]
        num_mov += 1
        mov_i += 1
    return num_mov

def find_gcd(x,y):
    while(y):
        x,y = y, x % y
    return x

def part2(inputfile):
    movs, graph = parser(inputfile)
    nodes = [x for x in graph if x[-1] == 'A']
    nums_mov = []

    for node in nodes:
        mov_i = 0
        num_mov = 0
        while node[-1] != 'Z':
            if mov_i >= len(movs):
                mov_i = 0
            mov = movs[mov_i]
            node = graph[node][mov]
            num_mov += 1
            mov_i += 1
        nums_mov.append(num_mov)
    gcd = find_gcd(nums_mov[0], nums_mov[1])
    for i in range(2, len(nums_mov)):
        gcd = find_gcd(gcd, nums_mov[i])

    val = 1
    for num in nums_mov:
        val = (val * num) / find_gcd(val, num)
    return val
    
if __name__ == '__main__':
    inputfile = open('day8.txt').readlines()
    sol1 = part1(inputfile)
    sol2 = part2(inputfile)
    print(f"Solution for part 1: {sol1}")
    print(f"Solution for part 2: {sol2}")
