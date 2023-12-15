memory = {}

def compute_single_value(elem,value):
    asc = ord(elem)
    value += asc
    value = value * 17
    value = value % 256
    return value

def compute_value(code,evaluated_code,value):
    if code:
        if evaluated_code == '':
            seen = []
            for k in range(2,len(code)-1):
                if ''.join(code[:k]) in memory:
                    seen.append(k)
            if seen:
                to_k = max(seen)
                seen_str = ''.join(code[:to_k])
                return compute_value(code[to_k:], seen_str, memory[seen_str])
        elem = code[0]
        code = code[1:]
        evaluated_code += elem
        value = compute_single_value(elem, value)
        memory[evaluated_code] = value
        value = compute_value(code, evaluated_code, value)
    return value

def part1(inputfile):
    steps = inputfile.split(',')
    totals = []
    for step in steps:
        totals.append(compute_value(step,'',0))
    return sum(totals)

def part2(inputfile):
    boxes = {}
    steps = inputfile.split(',')
    for step in steps:
        if '=' in step:
            step_split = step.split('=')
            s = step_split[0]
            box = compute_value(s, '', 0)
            if box in boxes:
                same_label = [i for i,x in enumerate(boxes[box]) if x[0] == s]
                if len(same_label):
                    boxes[box][same_label[0]] = step_split
                else:
                    boxes[box].append(step_split)
            else:
                boxes[box] = [step_split]
        else:
            step_split = step.split('-')
            s = step_split[0]
            box = compute_value(s, '', 0)
            if box in boxes:
                i_step_split = [i for i,x in enumerate(boxes[box]) if x[0] == s ]
                if len(i_step_split):
                    boxes[box].pop(i_step_split[0])
    v = 0
    for box in boxes:
        for i, x in enumerate(boxes[box]):
            v += (box + 1) * (i+1) * int(x[1])
    return v

if __name__ == '__main__':
    inputfile = open('day15.txt').read()
    sol1 = part1(inputfile)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
