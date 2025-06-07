def solve(l, r):
    if l > r//2: return -1, -1

    return r//2, (r//2)*2

for t in range(int(input())):
    l, r = (int(__) for __ in input().strip().split())

    print(*solve(l, r))