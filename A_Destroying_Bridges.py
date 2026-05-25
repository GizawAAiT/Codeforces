def solve(n: int, k: int) -> int:
    return 1 if k >= n-1 else n

for t in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))