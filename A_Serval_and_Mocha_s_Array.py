import math
from itertools import combinations
def solve(n: int, a: list[int]) -> str:
    # : N^2 sol:
    for a1, a2 in combinations(a, 2):
        if math.gcd(a1, a2) <= 2: return 'Yes'
    
    return 'No'

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    
    print(solve(n, a))