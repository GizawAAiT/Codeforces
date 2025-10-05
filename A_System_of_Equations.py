from math import sqrt

def solve(n: int, m: int):
    cnt = 0
    for a in range(m+n):
        c = a**2 + a - m - n

        if 1-4*c >= 0:
            b = (-1+sqrt(1-4*c))/2
            if b.is_integer() and a**2+b==n and a+b**2 == m:
                cnt += 1
                
    print(cnt)

n, m = (int(_) for _ in input().split())
solve(n, m)