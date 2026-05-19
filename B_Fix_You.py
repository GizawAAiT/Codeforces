def solve(grid: list[str]) -> int:
    """
    Grid represents direction (R, D only) of luggage movement.
    Returns:
        int: Min direction changes needed so that all luggage reaches (n, m)
    """
    
    # count Rs in the last col:
    count_R = 0
    for i in range(len(grid)-1):
        count_R += grid[i][-1] == 'R'
    
    # count Ds in the last row:
    count_D = 0
    for j in range(len(grid[0])-1):
        count_D += grid[-1][j] == 'D'
    
    return count_R + count_D

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        grid = [input() for _ in range(n)]
        print(solve(grid))