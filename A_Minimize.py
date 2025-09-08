def solve(a, b):
    return b-a

for t in range(int(input())):
    a, b = (int(_) for _ in input().split())
    print(solve(a, b))