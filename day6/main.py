def parsefile(inputfile):
    f = inputfile
    time = [int(y) for y in f[0].split(':')[1].split()]
    distance = [int(y) for y in f[1].split(':')[1].split()]
    return time, distance


def part1(inputfile):
    times, distances = parsefile(inputfile)
    num_won = []
    for i in range(len(times)):
        ways_to_win = 0
        time = times[i]
        distance = distances[i]
        for speed in range(time):
           t2 = time - speed
           travelled = t2 * speed 
           if travelled > distance:
               ways_to_win += 1
        num_won.append(ways_to_win)
    val = 1
    for n in num_won:
        val = val * n
    return val

def part2(inputfile):
    times, distances = parsefile(inputfile)
    actual_time = int(''.join([str(t) for t in times]))
    actual_distance = int(''.join([str(d) for d in distances]))
    ways_to_win = 0
    for speed in range(actual_time):
        t2 = actual_time - speed
        travelled = t2 * speed 
        if travelled > actual_distance:
            ways_to_win += 1
    return ways_to_win

if __name__ == '__main__':
    inputfile = open('./day6.txt').readlines()
    sol1 = part1(inputfile)
    sol2 = part2(inputfile)
    print(f"Solution for part 1: {sol1}")
    print(f"Solution for part 2: {sol2}")