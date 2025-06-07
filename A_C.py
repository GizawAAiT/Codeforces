def solve(a, b, n):
    _max = max(a, b)
    steps = 0

    while _max <= n:
        a, b = max(a, b), a + b 
        _max = max(a, b)
        steps += 1
    
    return steps

for T in range(int(input())):
    a, b, n = (int(_) for _ in input().split())

    print(solve(a, b, n))