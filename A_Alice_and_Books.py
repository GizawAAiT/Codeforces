def solve(n: int, a: list[int]) -> int:
    return max(a[:-1]) + a[-1]

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))