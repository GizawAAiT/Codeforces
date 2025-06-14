def solve(a, b, c, x, y):
    if max(0, x-a) + max(0, y- b) > c:
        return 'NO'
    
    return 'YES'

for t in range(int(input())):
    a, b, c, x, y = (int(_) for _ in input().split())
    
    print(solve(a, b, c, x, y))