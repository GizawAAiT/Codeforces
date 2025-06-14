def solve(a, b):
    if (1*a + 2*b) % 2 == 1: return 'NO'
    
    return "YES" if b % 2 == 0 or a > 0 else "NO"

for t in range(int(input())):
    a, b = (int(_) for _ in input().split())
    print(solve(
        a = a, b = b
    ))