def solve(l: int, r: int) -> int:
    if l == r == 1: return 1
    return r-l

for t in range(int(input())):
    l, r = map(int, input().split())
    print(solve(l, r))