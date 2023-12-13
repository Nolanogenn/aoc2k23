def parsefile(f):
    matrices = f.split('\n\n')
    rows = [[row for row in m.split('\n')] for m in matrices]
    cols = []
    for matrix in rows:
        matrix_cols = []
        l = len(matrix[0])
        for i in range(l):
            col = ''
            for r in matrix:
                col += r[i]
            matrix_cols.append(col)
        cols.append(matrix_cols)
    return rows, cols

def find_mirror(matrix):
    for i in range(1,len(matrix)):
        width = min(i, len(matrix)-i)
        x = matrix[i-width:i+width]
        half = len(x)//2
        if x[:half] ==  x[half:][::-1]:
            return i
    return 0

def part1(rows, cols):
    poss_rows = [find_mirror(r) for r in rows]
    poss_cols = [find_mirror(c) for c in cols]

    rows = [r*100 for i, r in enumerate(poss_rows) if r > poss_cols[i]]    
    cols = [c for i, c in enumerate(poss_cols) if c > poss_rows[i]]    

    x = sum(rows) + sum(cols)
    return x
    
def find_smudges(matrix):
    for i in range(len(matrix)):
        c1 = matrix[i]
        for k in range(len(matrix)):
            c2 = matrix[k]
            if len([x for p, x in enumerate(c1) if c2[p] != x]) == 1:
                return [i, k]
    return False

def find_mirror_with_smudges(matrix):
    for i in range(1,len(matrix)):
        width = min(i, len(matrix)-i)
        x = matrix[i-width:i+width]
        half = len(x)//2
        first_half = ''.join(x[:half])
        second_half = ''.join(x[half:][::-1])
        overlap = [x for i,x in enumerate(first_half) if second_half[i] != x]
        if len(overlap) == 1:
            return i
    return 0

def part2(rows, cols):
    poss_rows = [find_mirror_with_smudges(r) for r in rows]
    poss_cols = [find_mirror_with_smudges(c) for c in cols]

    rows = [r*100 for i, r in enumerate(poss_rows) if r > poss_cols[i]]    
    cols = [c for i, c in enumerate(poss_cols) if c > poss_rows[i]]    

    x = sum(rows) + sum(cols)
    return x
    
if __name__ == '__main__':
    inputfile = open('day13.txt').read()
    rows, cols = parsefile(inputfile)
    sol1 = part1(rows, cols)
    print(f"Solution for part 1: {sol1}")
    sol2 = part2(rows, cols)
    print(f"Solution for part 2: {sol2}")
