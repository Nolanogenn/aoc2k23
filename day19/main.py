import re
import pprint

def part1(workflows, parts):
    nodes = {}
    for step in workflows:
        nodes[step[0]] = []
        for branch in step[1]:
            if '<' in branch:
                data = branch.split('<')
                num,node = data[1].split(':')
                nodes[step[0]].append((data[0],'lower',int(num),node))
            elif '>' in branch:
                data = branch.split('>')
                num,node = data[1].split(':')
                nodes[step[0]].append((data[0],'higher',int(num),node))
            else:
                nodes[step[0]].append(('else', branch))
    accepted = []
    for part in parts:
        d_part = {
            p[0] : int(p[1])
            for p in part
        }
        pos = 'in' 
        while pos not in ['R', 'A']:
            check_list = [n for n in nodes[pos] if len(n) > 2]
            cs = [
                (d_part[c[0]] < c[2],c[3]) 
                if c[1] == 'lower' 
                else (d_part[c[0]] > c[2],c[3]) 
                for c in check_list]
            pos2 = [x[1] for x in cs if x[0]]
            if pos2:
                pos = pos2[0]
            else:
                pos = nodes[pos][-1][-1]
        if pos == 'A':
            accepted.append(sum(d_part.values()))
    return sum(accepted)

def part2(workflows):
    nodes = {}
    for step in workflows:
        nodes[step[0]] = []
        for branch in step[1]:
            if '<' in branch:
                data = branch.split('<')
                num,node = data[1].split(':')
                nodes[step[0]].append((data[0],'lower',int(num),node))
            elif '>' in branch:
                data = branch.split('>')
                num,node = data[1].split(':')
                nodes[step[0]].append((data[0],'higher',int(num),node))
            else:
                nodes[step[0]].append(('else', branch))
    pos = 'in'
    queue = [(pos, {"x":4000, "m":4000, "a":4000, "s":4000})]
    v = 0
    while queue:
        x = queue[0]
        pos = x[0]
        ns = x[1]
        branches = nodes[pos]
        for branch in branches:
            filtered = dict(ns)
            if x[0] != 'else':
                tofilter = branch[0]
                direction = branch[-1]
                filtered[tofilter] = ns[tofilter]-branch[2]
                new_branch = (direction, branch[2])
                queue.append(new_branch)
            else:
                direction = branch[-1]
                queue.append((direction, filtered))
    pass

if __name__ == '__main__':
    pattern = r'([a-z]*){(.*)}'
    pattern_part = r'([xmas])=([0-9]+)'
    workflows, parts = open('day19test.txt').read().split('\n\n')
    workflows = workflows.strip().split()
    workflows = [re.search(pattern, workflow).groups() for workflow in workflows]
    workflows = [(x[0],x[1].split(',')) for x in workflows]
    parts = parts.strip().split()
    parts = [re.findall(pattern_part, part) for part in parts]
    sol1 = part1(workflows, parts)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(workflows)
    print(f"Solution for part 2: {sol2}")
