def part1(inputfile):
    modules = {
        x[0]:x[1] for x in inputfile[1:]
    }
    status_dict = {
        x[0]:'off'  if x[1] == '%' else 'low' for x in inputfile[1:]}
    status = tuple((
        x[0],'off')  if x[1] == '%' else (x[0],'low') for x in inputfile[1:])
    seen = set()
    seen.add(status)
    print(seen)
    queue = [('low', x) for x in inputfile[0][1]]
    while queue :
        pulse, directions = queue[0]
        type_module = modules[direction]
        if type_module == '%':
            if pulse == 'high':
                pass
            else:
                if status_dict[direction] == 'off':
                    new_elem = ('high', direction)
        
    
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
