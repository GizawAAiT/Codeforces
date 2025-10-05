def solve(n, a, b):
    return min(n*a, (n//2)*b + (n%2)*a)

for t in range(int(input())):
    n, a, b = (int(_) for _ in input().split())
    print(solve(n, a, b))