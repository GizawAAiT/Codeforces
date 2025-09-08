def solve(a, b):
    return [b[0] + a[1:], a[0] + b[1:]]

for t in range(int(input())):
    a, b = (input().split())
    print(*solve(a, b))    