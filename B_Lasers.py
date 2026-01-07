def solve(n,m):
    return n+m

for t in range(int(input())):
    n, m, x, y = (int(_) for _ in input().strip().split())
    ns = [int(_) for _ in input().strip().split()]
    ms = [int(_) for _ in input().strip().split()]
    print(solve(n,m))