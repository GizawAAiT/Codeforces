def solve(n, m, grid):
    target = 'vika'
    indx = 0
    
    for col in range(m):
        for row in range(n):
            if grid[row][col] == target[indx]:
                indx += 1
                break
        
        if indx == 4: return "YES"
    
    return "NO"

for t in range(int(input())):
    n, m = (int(_) for _ in input().split())
    grid = [input() for _ in range(n)]
    print(solve(n, m, grid))
                