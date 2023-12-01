inputfile = open('./input').readlines()

def part1(inputfile):
   nums = [
           [char for char in line if char.isnumeric()]
           for line in inputfile
           ]
   nums = [int(''.join([num[0], num[-1]])) for num in nums]
   return sum(nums)

def part2(inputfile):
    dict_digits = {
            'one' : 'o1e',
            'two' : 't2o',
            'three' : 't3e',
            'four' : 'f4r',
            'five' : 'f5e', 
            'six' : 's6x',
            'seven' : 's7n',
            'eight' : 'e8t',
            'nine' : 'n9n'
            }
    lines = []
    for line in inputfile:
        clean_line = str(line)
        for digit in dict_digits:
            clean_line = clean_line.replace(digit, dict_digits[digit])
        lines.append(clean_line)
    solution = part1(lines)
    return solution

if __name__ == '__main__':
#    sol1 = part1(inputfile)
#    print(f"Solution for part 1: {sol1}")
    sol2 = part2(inputfile)
    print(f"Solution for part 2: {sol2}")



