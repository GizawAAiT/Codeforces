from math import sqrt, ceil

def solve(l: int, r: int) -> int:
    
    n = r-l+1
    
    x = (-1 + (sqrt(1 + 8*n)))/2
    return ceil(x)

for _ in range(int(input())):
    l, r = map(int, input().split())
    print(solve(l, r))