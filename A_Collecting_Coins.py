def solve(a, b, c, n):
    _max = max(a, b, c)
    min_req = 3*_max - (a+b+c)
    if n < min_req or (n-min_req) % 3 != 0:
        return 'NO'
    
    return 'YES'

for t in range(int(input())):
    a, b, c, n = (int(_) for _ in input().split())
    print(solve(a,b,c,n))