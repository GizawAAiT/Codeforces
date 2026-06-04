def solve(n: int, s: list[int]) -> int:
    _mex = s.count(0)
    
    return sum(s) + _mex

for t in range(int(input())):
    n = int(input())
    s = [int(_) for _ in input().split()]
    print(solve(n, s))