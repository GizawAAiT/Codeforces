def solve(n, m, photo_grid):
    for r in range(n):
        for c in range(m):
            if photo_grid[r][c] in 'CMY':
                return '#Color'
    
    return '#Black&White'

n, m = (int(_) for _ in input().split())
photo_grid = []
for _ in range(n):
    row = input().split()
    photo_grid.append(row)
    
print(solve(n, m, photo_grid))