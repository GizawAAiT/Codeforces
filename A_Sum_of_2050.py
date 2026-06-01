from math import log, floor

def solve(n: int) -> int:
    if n % 2050: return -1
    
    return sum(int(digit) for digit in str(n//2050))

for T in range(int(input())):
    n = int(input())
    print(solve(n))