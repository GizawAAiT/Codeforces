def solve(a: int, b: int, x: int, y: int, n: int):
    if x > y:
        a, b = b, a
        x, y = y, x

    diff = min(a-x, n)
    a -= diff
    n -= diff

    diff = min(b-y, n)
    b -= diff
    
    return a*b

for t in range(int(input())):
    a, b, x, y, n = (int(_) for _ in input().split())
    print(solve(a, b, x, y, n))
    