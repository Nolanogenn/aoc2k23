import re

def mullist(l):
    x = 1
    for elem in l:
        x *= elem
    return x

def parseinput(inputfile):
    max_counts = {
            'red' : 12,
            'green' : 13,
            'blue' : 14
            }
    splitlines = {}
    for line_i,line in enumerate(inputfile):
        games = line.split()
        games = ' '.join(games[2:])
        games = games.split(';')
        splitlines[line_i + 1] = []
        for game in games:
            colors = re.findall(r'(green|blue|red)', game)
            balls = re.findall(r'([0-9]+)', game)
            zipped = zip(colors, balls)
            
            game_dict = {
                    x[0] : (int(x[1]), int(x[1]) <= max_counts[x[0]])
                    for x in zipped
                    }
            splitlines[line_i + 1].append(game_dict)
    return splitlines

def part1(inputfile):
    splitlines = parseinput(inputfile)
    good_ids = [x for x in splitlines if all([k[color][1] for k in splitlines[x] for color in k])]
    return(sum(good_ids))

def part2(inputfile):
    splitlines = parseinput(inputfile)
    min_balls_total = {}
    for game in splitlines:
        min_balls = {}
        for slot in splitlines[game]:
            for color in slot:
                if color not in min_balls:
                    min_balls[color] = slot[color][0]
                else:
                    min_balls[color] = max(min_balls[color], slot[color][0])
        min_balls_total[game] = min_balls
    power = [
            mullist([min_balls_total[x][color] for color in min_balls_total[x]])
            for x in min_balls_total
            ]
    return sum(power)

if __name__ == '__main__':
    file = open('input').readlines()
    sol1 = part1(file)
    print(f"First solution: {sol1}")
    sol2 = part2(file)
    print(f"First solution: {sol2}")
