def solve(n: int, m: int, a: list[int]) -> int:
    return max(0, sum(a) - m)

for t in range(int(input())):
    n, m = map(int, input().split())
    a = [int(_) for _ in input().split()]
    print(solve(n, m, a))