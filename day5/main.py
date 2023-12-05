def parsefile(file):
    parsedfile = file.split('\n\n')
    return parsedfile

def part1(inputfile):
    parsedfile = parsefile(inputfile)
    print(parsedfile)
    pass
def part2(inputfile):
    pass


if __name__ == '__main__':
    inputfile = open('day5test.txt').read()
    sol1 = part1(inputfile)
    sol2 = part2(inputfile)

    print(f"Solution for part1: {sol1}")
    print(f"Solution for part2: {sol2}")