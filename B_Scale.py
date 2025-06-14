def solve(grid: list[str], k: int):
    res = []
    for row in range(len(grid)//k):
        
        pattern = ''
        for col in range(len(grid[0])//k):
            pattern += grid[(row + 1)*k - 1][(col + 1)* k - 1]
        
        res.append(pattern)
    
    return res

for t in range(int(input())):
    n, k = (int(_) for _ in input().strip().split())
    grid: list[str] = []
    for _ in range(n):
        grid.append(input().strip())
    
    result = solve(
        grid= grid,
        k= k
    )
    
    for res in result:
        print(res)