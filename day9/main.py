def get_diffs(l):
    return [l[i]-l[i-1] for i in range(1, len(l))]

def part1(inputfile):
    inputfile = [[int(n) for n in l.split()] for l in inputfile]
    val = 0
    for l in inputfile:
        line = l
        lines = [line]
        while not all([i == 0 for i in line]):
            line = get_diffs(line)
            lines.append(line)
        num_to_add = 0
        for i, sequence in enumerate(lines[::-1]):
            to_append = sequence[-1]+num_to_add
            num_to_add = to_append
        val += to_append
    return val
def part2(inputfile):
    inputfile = [[int(n) for n in l.split()] for l in inputfile]
    val = 0
    for l in inputfile:
        line = l
        lines = [line]
        while not all([i == 0 for i in line]):
            line = get_diffs(line)
            lines.append(line)
        num_to_add = 0
        for i, sequence in enumerate(lines[::-1]):
            to_append = sequence[0]-num_to_add
            num_to_add = to_append
        val += to_append
    return val
if __name__ == '__main__':
    inputfile = open('day9bigboi.txt').readlines()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
