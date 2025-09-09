def solve(grid):
    
    def point(i, j):
        left_right = min(j-0, 9-j)
        top_bottom = min(i-0, 9-i)
        return min(left_right, top_bottom) + 1
    
    total = 0
    for i in range(10):
        for j in range(10):
            total += point(i, j) if grid[i][j] == 'X' else 0
    
    return total

for t in range(int(input())):
    grid = []
    for _ in range(10):
        grid.append(input())
    
    print(solve(grid))