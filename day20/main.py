def part1(inputfile):
    modules = {
        x[0]:(x[1], x[2]) for x in inputfile[1:]
    }
    modules['start'] = ('none', inputfile[0][1])
    status = {
        k : 'off' for k in modules if modules[k][1][0] == '%'
    }
    for module in modules:
        if modules[module] == '&':
            connections = [m for m in modules if module in modules[m][1][1]]
            print(module, connections)
    
    while queue :
        pulse, directions = queue[0]
        for direction in directions:
            type_module = modules[direction]
            if type_module == '%':
                if pulse == 'high':
                    pass
                else:
                    if status_dict[direction] == 'off':
                        new_elem = ('high', direction)
                        queue.append(new_elem)
        
    
    pass
def part2(inputfile):
    pass

if __name__ == '__main__':
    inputfile = open('day20test.txt').readlines()
    modules = [x.strip().split(' -> ') for x in inputfile]
    modules[0] = (modules[0][0], [y for y in modules[0][1]])
    modules[1:] = [(x[0][1:], x[0][0], [y for y in x[1].split(',')]) for x in modules[1:]]
    sol1 = part1(modules)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")
