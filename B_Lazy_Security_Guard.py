from math import ceil, sqrt, floor
def solve(n):
    if ceil(sqrt(n)) == sqrt(n):
        return 4*sqrt(n)
    
    res = 4*ceil(sqrt(n))
    if n - 4*floor(sqrt(n)) < floor(sqrt(n)):
        res -= 2
    return res

print(int(solve(int(input()))))