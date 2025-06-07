from math import ceil

def solve(a, b, c):
    diff = abs(b-a)

    return ceil((diff/2)/c)

for _ in range(int(input())): # Test t
    a, b, c = (int(_) for _ in input().split())
    print(solve(a, b, c))