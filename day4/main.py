import re

def parsefile(inputfile):
    pattern = r'([0-9]+)'
    split_lines = [
            line.split('|') for line in inputfile
            ]
    num_winning = [re.findall(pattern, x[0])[1:] for x in split_lines]
    num_have = [re.findall(pattern, x[1]) for x in split_lines]
    
    return list(zip(num_winning,num_have))

def part1(inputfile):
    parsed = parsefile(inputfile)
    num_won = [
            [num for num in x[0] if num in x[1]]
            for x in parsed
            ]
    val = 0
    for won in num_won:
        if len(won) > 0:
            won_val = 1
            for num in won[1:]:
                won_val *= 2
            val += won_val
    return val
    
def part2(inputfile):
    parsed = parsefile(inputfile)
    num_won = [
            [num for num in x[0] if num in x[1]]
            for x in parsed
            ]
    num_copies = {
            i+1 : 1
            for i in range(len(parsed))
            }
    for i,game in enumerate(parsed):
        won = len(num_won[i])
        for v in range(won):
            if i+v+2 in num_copies:
                num_copies[i+v+2] += 1*num_copies[i+1]
    toreturn = sum([num_copies[x] for x in num_copies])
    return toreturn

if __name__ == '__main__':
    inputfile = open('day4.txt').readlines()
    sol1 = part1(inputfile)
    sol2 = part2(inputfile)
    print(f"Solution to part 1: {sol1}")
    print(f"Solution to part 2: {sol2}")
