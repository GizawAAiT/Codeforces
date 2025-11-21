def solve(n: int) -> str:
    return 'Alice' if n % 4 else 'Bob'

for t in range(int(input())):
    n = int(input())
    print(solve(n))