def solve(n, m):
    return min(2, n-1)*m

for t in range(int(input())):
    n, m = (int(_) for _ in input().split())
    print(solve(
        n=n,
        m=m
    ))