def part1(inputfile):
    modules = {
        x[0]:(x[1], x[2]) for x in inputfile[1:]
    }
    modules['start'] = ('none', inputfile[0][1])
    status = {
        k : 'off' for k in modules if modules[k][0] == '%'
    }
    status['start'] = 'on'
    for module in modules:
        if modules[module][0] == '&':
            connections = [m for m in modules if module in modules[m][1]]
            status[module] = {c:'low' for c in connections}

    starting_status = dict(status) 
    low_sent = 0
    high_sent = 0
    times_pressed = 0
    sent_dict = {
            0 : {
                'low' : low_sent,
                'high' : high_sent}
            }
    while True:
        start = ('low', 'start', 'start')
        queue = [start]
        times_pressed += 1
        while queue :
            pulse, position, previous_module = queue[0]
            if pulse == 'high':
                high_sent += 1
            else:
                low_sent += 1
            if position not in modules:
                type_module = 'None'
                move_on = False
                pass
            else:
                directions = modules[position][1]
                type_module = modules[position][0]
                move_on = True
            if type_module == '%':
                if pulse == 'high':
                    move_on = False
                else:
                    if status[position] == 'off':
                        status[position] = 'on'
                        new_pulse = 'high'
                    else:
                        status[position] = 'off'
                        new_pulse = 'low'
            elif type_module == '&':
                status[position][previous_module] = pulse
                if all([x == 'high' for x in status[position].values()]):
                    new_pulse = 'low'
                else:
                    new_pulse = 'high'
            else:
                new_pulse = pulse
            if move_on:
                for direction in directions:
                    new_elem = (new_pulse, direction, position)
                    queue.append(new_elem)
            queue = queue[1:]
        sent_dict[times_pressed] = {
                    'low' : low_sent,
                    'high' : high_sent
                    }
        if status == starting_status or times_pressed == 1000:
            break

    loops = 1000 // times_pressed
    remaining = 1000 % times_pressed
    highs = (high_sent * loops) + sent_dict[remaining]['high']
    lows = (low_sent * loops) + sent_dict[remaining]['low']
    return highs * lows

def part2(inputfile):
    modules = {
        x[0]:(x[1], x[2]) for x in inputfile[1:]
    }
    modules['start'] = ('none', inputfile[0][1])
    status = {
        k : 'off' for k in modules if modules[k][0] == '%'
    }
    status['start'] = 'on'
    for module in modules:
        if modules[module][0] == '&':
            connections = [m for m in modules if module in modules[m][1]]
            status[module] = {c:'low' for c in connections}
    get_to = 'rx'
    conjunction = [x for x in modules if get_to in modules[x][1]][0]
    conjunction_modules_cycles = {}
    starting_status = dict(status) 
    low_sent = 0
    high_sent = 0
    times_pressed = 0
    sent_dict = {
            0 : {
                'low' : low_sent,
                'high' : high_sent}
            }
    while times_pressed < 5000:
        start = ('low', 'start', 'start')
        queue = [start]
        times_pressed += 1
        sent = []
        while queue :
            pulse, position, previous_module = queue[0]
            if pulse == 'high':
                high_sent += 1
            else:
                low_sent += 1
            if position not in modules:
                type_module = 'None'
                move_on = False
                pass
            else:
                directions = modules[position][1]
                type_module = modules[position][0]
                move_on = True
            if type_module == '%':
                if pulse == 'high':
                    move_on = False
                else:
                    if status[position] == 'off':
                        status[position] = 'on'
                        new_pulse = 'high'
                    else:
                        status[position] = 'off'
                        new_pulse = 'low'
            elif type_module == '&':
                status[position][previous_module] = pulse
                if all([x == 'high' for x in status[position].values()]):
                    new_pulse = 'low'
                    if position not in conjunction_modules_cycles:
                        conjunction_modules_cycles[position] = times_pressed
                else:
                    new_pulse = 'high'
            else:
                new_pulse = pulse
            if move_on:
                for direction in directions:
                    new_elem = (new_pulse, direction, position)
                    sent.append(new_elem)
                    queue.append(new_elem)
            queue = queue[1:]
    v = 1
    for k in conjunction_modules_cycles:
        v = v * conjunction_modules_cycles[k]
    return v

if __name__ == '__main__':
    inputfile = open('day20.txt').readlines()
    modules_raw = [x.strip().split(' -> ') for x in inputfile]
    broadcast = [x for x in modules_raw if x[0] == 'broadcaster'][0]
    modules = [(broadcast[0], [x.strip() for x in broadcast[1].split(',')])]
    modules_toappend = [(x[0][1:], x[0][0], [y.strip() for y in x[1].split(',')]) for x in modules_raw if x[0] != 'broadcaster']
    modules.extend(modules_toappend)
    sol1 = part1(modules)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(modules)
    print(f"Solution for part 2: {sol2}")
