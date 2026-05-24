def solve(x, y):
    return 'YES' if y >= -1 else 'NO'

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(solve(x, y))