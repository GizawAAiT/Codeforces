def solve(grid):
    output = ''
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] != '.':
                output += grid[r][c]
    
    print(output)
    
for t in range(int(input())):
    inp = []
    for _ in range(8):
        inp.append(input().strip())
    
    solve(inp)