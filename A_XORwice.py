def solve(a, b):
    return a^b

for _ in range(int(input())):
    a, b = (int(_) for _ in input().strip().split())
    print(solve(a, b)
)