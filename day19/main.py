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
                nodes[step[0]].append(('else',branch))

    queue = [('in', {"x":(1,4000), "m":(1,4000), "a":(1,4000), "s":(1,4000)})]
    A = []
    while len(queue) > 0:
        pos, original = queue.pop()
        for branch in nodes[pos]:
            if 'else' not in branch:
                tofilter, operation, threshold, direction = branch
                tmp_part = original.copy()
                if operation == 'lower':
                    tmp_part[tofilter] = (tmp_part[tofilter][0], threshold-1)
                    original[tofilter] = (threshold, original[tofilter][1])
                elif operation == 'higher':
                    tmp_part[tofilter] = (threshold+1, tmp_part[tofilter][1])
                    original[tofilter] = (original[tofilter][0], threshold)
                if direction in ["A", "R"]:
                    if direction=="A":
                        A.append(tmp_part.copy())
                else:
                    queue.append((direction, tmp_part.copy()))
            else:
                direction = branch[-1]
                if direction in ["A", "R"]:
                    if direction=="A":
                        A.append(original.copy())
                else:
                    queue.append((direction, original.copy()))

    val =0
    for part in A:
        v = 1
        for j in part.values():
            v *= j[1] - j[0]+1
        val += v
    return val

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
    sol2 = part2(workflows)
    print(f"Solution for part 2: {sol2}")
