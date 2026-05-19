def solve(r: int, c: int, grid: list[str]) -> int:
    """
    - 
    """
    evil_strawberry_rows, evil_strawberry_cols = set(), set()
    
    for row in range(r):
        for col in range(c):
            if grid[row][col] != '.': # if not empty
                evil_strawberry_rows.add(row)
                evil_strawberry_cols.add(col)
    
    # count:
    count = 0
    for row in range(r):
        for col in range(c):
            if not (
                row in evil_strawberry_rows and col in evil_strawberry_cols
            ): count += 1
                
    return count

if __name__ == "__main__":
    r, c = map(int, input().strip().split())
    grid = []
    for _ in range(r):
        grid.append(input().strip())
    
    print(solve(r, c, grid))