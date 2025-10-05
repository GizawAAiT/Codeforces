def solve(n):
    double_hash_sign = '##'
    double_dot_sign = '..'
    
    grid = []
    for row in range(n):
        r = ''
        for col in range(n):
            if (row + col) % 2 == 0:
                r += double_hash_sign
            else: r += double_dot_sign
        
        grid.append(r)
        grid.append(r)
    
    for row in grid:
        print(row)

for t in range(int(input())):
    n = int(input())
    solve(n)