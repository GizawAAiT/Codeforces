def solve(h, m):
    return (23-h)*60 + (60-m)

for t in range(int(input())):
    h, m = (int(_) for _ in input().split())
    print(solve(h, m))