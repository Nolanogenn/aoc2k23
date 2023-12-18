directions = {
        'R' : (0,1),
        'L' : (0, -1),
        'U' : (-1, 0),
        'D' : (1, 0)
        }
reflections = {
        'R' : {
            '/' : 'U',
            '\\' : 'D'
            },
        'L' : {
            '/' : 'D',
            '\\' : 'U'
            },
        'U' : {
            '/' : 'R',
            '\\' : 'L'
            },
        'D' : {
            '/' : 'L',
            '\\' : 'R'
            }
        }
def check(point, max_x, max_y):
    m_point = min(point)
    if m_point < 0:
        return False
    if point[0] >= max_y or point[1] >= max_x:
        return False
    return True
        
def part1(inputfile, starting_pos, starting_mov):
    grid = [x.strip() for x in inputfile]
    max_x = len(grid[0])
    max_y = len(grid)
    pos = starting_pos
    tocheck = [(pos,starting_mov)]
    visited = set()
    energized = set()
    while tocheck:
        pos, direction = tocheck[0]
        visited.add(tocheck[0])
        energized.add(pos)
        pos_symbol = grid[pos[0]][pos[1]]
        d = directions[direction]
        if pos_symbol == '.':
            next_pos = (
                    pos[0]+d[0],
                    pos[1]+d[1]
                    )
            if check(next_pos, max_x, max_y) and (next_pos,direction) not in visited:
                tocheck.append((next_pos, direction))
        elif pos_symbol == '|':
            if direction in ['R', 'L']:
                next_pos_1 = (
                        min(max(pos[0]-1,0),max_y),
                        pos[1]
                        )
                next_pos_2 = (
                        min(max(pos[0]+1,0),max_y),
                        pos[1]
                        )
                if check(next_pos_1, max_x, max_y) and (next_pos_1, 'U') not in visited:
                    tocheck.append((next_pos_1, 'U'))
                if check(next_pos_2, max_x, max_y) and (next_pos_2, 'D') not in visited:
                    tocheck.append((next_pos_2, 'D'))
            else:
                next_pos = (
                        pos[0]+d[0],
                        pos[1]+d[1]
                        )
                if check(next_pos, max_x, max_y) and (next_pos, direction) not in visited:
                    tocheck.append((next_pos, direction))
        elif pos_symbol == '-': 
            if direction in ['U', 'D']:
                next_pos_1 = (
                        pos[0],
                        pos[1]-1,
                        )
                next_pos_2 = (
                        pos[0],
                        pos[1]+1,
                        )
                if check(next_pos_1, max_x, max_y) and (next_pos_1, 'L') not in visited:
                    tocheck.append((next_pos_1, 'L'))
                if check(next_pos_2, max_x, max_y) and (next_pos_2, 'R') not in visited:
                    tocheck.append((next_pos_2, 'R'))
            else:
                next_pos = (
                        pos[0]+d[0],
                        pos[1]+d[1]
                        )
                if check(next_pos, max_x, max_y) and (next_pos, direction) not in visited:
                    tocheck.append((next_pos, direction))
        elif pos_symbol in ['/','\\']:
            new_direction = reflections[direction][pos_symbol]
            mov = directions[new_direction]
            next_pos = (
                    pos[0]+mov[0],
                    pos[1]+mov[1]
                    )
            if check(next_pos, max_x, max_y) and (next_pos, new_direction) not in visited:
                tocheck.append((next_pos, new_direction))
        tocheck = tocheck[1:]
    return len(energized)

def part2(inputfile):
    starting_pos = []
    all_energized = []
    grid = [x.strip() for x in inputfile]

    pos_d = [((0, x), 'D') for x in range(len(grid))]
    pos_u = [((len(grid)-1, x), 'U') for x in range(len(grid))]
    pos_r = [((x, 0), 'R') for x in range(len(grid[0]))]
    pos_l = [((x, len(grid[0])-1), 'L') for x in range(len(grid[0]))]

    all_pos = pos_d + pos_u + pos_r + pos_l
    for pos in all_pos:
        all_energized.append(part1(inputfile, pos[0], pos[1]))
    return max(all_energized)

if __name__ == '__main__':
    inputfile = open('day16.txt').readlines()
    sol1 = part1(inputfile, (0,0), 'R')
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
