def solve(n: int) -> int:
    return 2**n - 1

for t in range(int(input())):
    n = int(input())
    print(solve(n))