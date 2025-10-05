def solve(n):
    grid =[[1 for _ in range(n)] for _ in range(n)]
    for row in range(1, n):
        for col in range(1, n):
            grid[row][col] = grid[row-1][col] + grid[row][col-1]
    
    return grid[n-1][n-1]
    
n = int(input())
print(solve(n))