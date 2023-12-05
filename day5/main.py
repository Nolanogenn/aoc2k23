from tqdm import tqdm

def parsefile(file):
    parsedfile = file.split('\n\n')
    seeds = [int(x) for x in parsedfile[0].split(':')[1].split()]
    steps = [
        x.split(':')[1].split('\n')[1:]
        for x in parsedfile[1:]
    ]
    steps = [
        list([int(n) for n in y.split()] for y in x)
        for x in steps 
    ]
    return seeds, steps

def check_step_part1(seed, step):
    for line in step:
        if seed >= line[1] and seed <= line[1]+line[2]:
            return line[0] + seed - line[1]
    return seed

def check_step_part2(seed, step):
    for line in step:
        if seed >= line[0] and seed <= line[0]+line[2]:
            return line[1] + seed - line[0]
    return seed

def part1(inputfile):
    seeds, steps = parsefile(inputfile) 
    locations = []
    for seed in seeds:
        for step in steps:
            seed = check_step_part1(seed, step)
        locations.append(seed)
    return min(locations)

def part2(inputfile):
    seeds, steps = parsefile(inputfile) 
    steps = steps[::-1]

    seed_ranges_start = seeds[::2]
    seed_ranges_end = seeds[1::2]
    seed_ranges_end = [
        seed_ranges_end[i] + seed_ranges_start[i]
        for i in range(len(seed_ranges_end))
    ]
    seed_ranges = list(zip(seed_ranges_start, seed_ranges_end))
    seed_ranges.sort(key=lambda x : x[0])
    found = False

    current_location = 0
    val = 0
    while not found:
        print(val, end='\r')
        for step in steps:
            val = check_step_part2(val, step)
        for r in seed_ranges:
            if val >= r[0] and val <= r[1]:
                found = True
                return current_location
        current_location += 1
        val = int(current_location)


if __name__ == '__main__':
    inputfile = open('day5.txt').read()
    sol1 = part1(inputfile)
    sol2 = part2(inputfile)

    print(f"Solution for part1: {sol1}")
    print(f"Solution for part2: {sol2}")