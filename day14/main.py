import pprint
import functools
import re

def parserows(inputfile):
    rows = []
    f = [x.strip() for x in inputfile]
    for i_row in range(len(f[0])):
        tmp = ''
        for r in inputfile:
            tmp += r[i_row]
        rows.append(tmp)
    return rows

def part1(inputfile):
    cols = parserows(inputfile)
    pattern = '[O]'
    loads = []
    for c in cols:
        idx_stones = [
                m.start(0) for m in re.finditer(pattern, c)
                ]
        for stone in idx_stones:
            num_mov = 0
            tocheck = c[:stone][::-1]
            num_mov = getnewpos(num_mov, tocheck)
            load = len(c) - stone + num_mov
            loads.append(load)
    return sum(loads)

def getnewpos(mov, tocheck):
    if tocheck:
        elem = tocheck[0]
        tocheck = tocheck[1:]
        if elem == '.':
            mov = getnewpos(mov+1, tocheck)
        if elem == '#':
            return mov
        if elem == 'O':
            mov = getnewpos(mov, tocheck)
    return mov


def change_mov(line, pos):
    tocheck = line[:pos][::-1]
    num_mov = getnewpos(0, tocheck)
    return num_mov

def cycle(
        inputfile,
        clean_inputfile,
        stones):
    north_comb = parserows([''.join(x) for x in inputfile])
    mov_north = [
            change_mov(north_comb[stone[1]],stone[0]) 
            for stone in stones
            ]
    stones = [(max(stone[0]-mov_north[i],0), stone[1]) for i, stone in enumerate(stones)]
    for stone in stones:
        clean_inputfile[stone[0]][stone[1]] = 'O'
    west_comb = [x for x in clean_inputfile]
    mov_west = [change_mov(west_comb[stone[0]],stone[1]) for stone in stones]
    stones = [(stone[0], max(stone[1]-mov_west[i],0)) for i, stone in enumerate(stones)]
    clean_inputfile = [list(r.strip().replace('O','.')) for r in inputfile]
    for stone in stones:
        clean_inputfile[stone[0]][stone[1]] = 'O'
    north_comb = parserows([''.join(x) for x in clean_inputfile])
    south_comb = [x[::-1] for x in north_comb]
    mov_south =[change_mov(south_comb[stone[1]],-stone[0]-1) for stone in stones]
    stones = [(min(stone[0]+mov_south[i],len(south_comb[stone[1]])-1), stone[1]) for i, stone in enumerate(stones)]
    clean_inputfile = [list(r.strip().replace('O','.')) for r in inputfile]
    for stone in stones:
        clean_inputfile[stone[0]][stone[1]] = 'O'
    east_comb = [x[::-1] for x in clean_inputfile]
    mov_east = [change_mov(east_comb[stone[0]],-stone[1]-1) for stone in stones]
    clean_inputfile = [list(r.strip().replace('O','.')) for r in inputfile]
    stones = [
            (stone[0], min(stone[1]+mov_east[i],len(east_comb[stone[0]])-1)) for i, stone in enumerate(stones)]
    for stone in stones:
        clean_inputfile[stone[0]][stone[1]] = 'O'
    return clean_inputfile, stones

seen_combinations = {}
def part2(inputfile):
    stones = []
    for i_r, row in enumerate(inputfile):
        for i_c, col in enumerate(row):
            if col =='O':
                stones.append((i_r, i_c))
    cycles = 1_000_000_000
    tilts_str = ''.join([''.join(x) for x in inputfile])
    clean_inputfile = [list(r.strip().replace('O','.')) for r in inputfile]
    tilts_input = inputfile
    current_cycles = 0
    while tilts_str not in seen_combinations:
        seen_combinations[tilts_str] = current_cycles
        current_cycles += 1
        tilts, stones = cycle(
                tilts_input,
                clean_inputfile,
                stones
                )
        tilts_str = '\n'.join([''.join(x) for x in tilts])
        tilts_input = [''.join(x) for x in tilts]
        clean_inputfile = [
                [c if c != 'O' else '.' for c in r ]
                for r in tilts_input
                ]

    start_from = seen_combinations[tilts_str]
    iterations = current_cycles-start_from
    loops = cycles-start_from
    outside_loops = loops % iterations
    pattern = r'[O]'
    to_compute = [x for x in seen_combinations if seen_combinations[x] == start_from + outside_loops][0]
    loads = []
    cols = parserows(to_compute.split('\n'))
    for c in cols:
        idx_stones = [
                m.start(0) for m in re.finditer(pattern, c)
                ]
        for stone in idx_stones:
            load = len(cols[0]) - stone
            loads.append(load)
    return sum(loads)

if __name__ == '__main__':
    inputfile = open('day14.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
