def solve(a,b,c,d):
    return [b, c, c]

for t in range(int(input())):
    a,b,c,d = [int(_) for _ in input().split()]
    print(*solve(a,b,c,d))