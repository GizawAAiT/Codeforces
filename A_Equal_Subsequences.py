def solve(n: int, k: int) -> str:
    return '1'*k + '0'*(n-k)

for t in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))