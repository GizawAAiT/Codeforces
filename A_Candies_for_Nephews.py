def solve(n: int) -> int:
    return 3 - n%3 if n%3 else 0

for t in range(int(input())):
    n = int(input())
    print(solve(n))