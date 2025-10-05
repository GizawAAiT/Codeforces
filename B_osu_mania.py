def solve(n, grid):
    indices = []
    for r in range(n-1, -1, -1):
        for col in range(4):
            if grid[r][col] == '#': indices.append(col+1)
    
    return indices

for t in range(int(input())):
    n = int(input())
    grid = []
    for row in range(n):
        grid.append(input().strip())
    
    print(*solve(n, grid))