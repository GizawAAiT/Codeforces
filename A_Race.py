def solve(a: int, x: int, y: int) -> str:
    """
    Return YES, NO depends on whether Bob can chose a position b such that
    its guaranteed he can reach either at x or y faster than Alice who is 
    currently at a.
    """
    
    if a < x and a < y or a > x and a > y:
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    a, x, y =map(int, input().split())
    print(solve(a, x, y))