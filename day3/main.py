import re

def parseinput(inputfile):
    engine_nums = {}
    engine_symbols = {}
    pattern = r'([0-9]+)|([^\.\n])'
    for i, line in enumerate(inputfile):
        matches = re.finditer(pattern, line)
        for x in matches:
            if x.group().isnumeric():
                engine_nums[(i, x.start()), (i, x.end()-1)] = x.group()
            else:
                engine_symbols[(i, x.start())] = x.group()
    return engine_nums, engine_symbols

pos_calc = [
        (-1, 0),
        (0, -1),
        (+1, 0),
        (0, +1),
        (+1, +1),
        (-1, -1),
        (-1, +1),
        (+1, -1)
        ]

def part1(inputfile):
    numbers, symbols = parseinput(inputfile)
    val = 0
    for pos in symbols:
        possible_adjacency = [(pos[0] + x[0], pos[1] + x[1]) for x in pos_calc]
        adjacent_numbers = [
                int(numbers[pos])
                for pos in numbers
                if pos[0] in possible_adjacency or pos[1] in possible_adjacency
                ]
        val += sum(adjacent_numbers)
    return val

def part2(inputfile):
    numbers, symbols = parseinput(inputfile)
    symbols_gear = {
            pos:symbols[pos] for pos in symbols if symbols[pos] == '*'
            }
    val_gear = 0
    for gear_pos in symbols_gear:
        possible_adjacency = [(gear_pos[0] + x[0], gear_pos[1] + x[1]) for x in pos_calc]
        adjacent_numbers = [
                int(numbers[pos])
                for pos in numbers
                if pos[0] in possible_adjacency or pos[1] in possible_adjacency
                ]
        if len(adjacent_numbers) == 2:
            value = adjacent_numbers[0] * adjacent_numbers[1]
            val_gear += value
    return val_gear

if __name__ == '__main__':
    inputfile = open('day3.txt').readlines()
    sol1 = part1(inputfile)
    sol2 = part2(inputfile)
    print(f"part 1 solution: {sol1}")
    print(f"part 2 solution: {sol2}")

