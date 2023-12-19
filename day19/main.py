import re

def part1(workflows, parts):
    nodes = {}
    for step in workflows:
        nodes[step[0]] = {}
        for branch in step[1]:
            if '<' in branch:
                data = branch.split('<')
                num,node = data[1].split(':')
                nodes[step[0]][data[0]] = {'lower' : int(num), 'child' : node}
            elif '>' in branch:
                data = branch.split('>')
                num,node = data[1].split(':')
                nodes[step[0]][data[0]] = {'higher' : int(num), 'child' : node}
            else:
                nodes[step[0]]['else'] = branch
    accepted = []
    for part in parts:
        d_part = {
            p[0] : int(p[1])
            for p in part
        }
        pos = 'in' 
        while pos not in ['R', 'A']:
            check_list = [x for x in nodes[pos] if x != 'else']
            for tocheck in check_list:
                val = d_part[tocheck]
                if 'lower' in nodes[pos][tocheck]:
                    if val < nodes[pos][tocheck]['lower']:
                        pos = nodes[pos][tocheck]['child']
                        break
                else:
                    if val > nodes[pos][tocheck]['higher']:
                        pos = nodes[pos][tocheck]['child']
                        break
            else:
                pos = nodes[pos]['else']
        if pos == 'A':
            accepted.append(sum(d_part.values()))
    return sum(accepted)
def part2(workflows, parts):
    pass

if __name__ == '__main__':
    pattern = r'([a-z]*){(.*)}'
    pattern_part = r'([xmas])=([0-9]+)'
    workflows, parts = open('day19.txt').read().split('\n\n')
    workflows = workflows.strip().split()
    workflows = [re.search(pattern, workflow).groups() for workflow in workflows]
    workflows = [(x[0],x[1].split(',')) for x in workflows]
    parts = parts.strip().split()
    parts = [re.findall(pattern_part, part) for part in parts]
    sol1 = part1(workflows, parts)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(workflows, parts)
    print(f"Solution for part 2: {sol2}")
