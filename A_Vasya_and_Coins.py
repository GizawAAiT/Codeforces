def solve(a, b):
    if a == 0: return 1

    return 2*b + a + 1

for t in range(int(input())):
    a, b = (int(_) for _ in input().strip().split())
    print(solve(a, b))