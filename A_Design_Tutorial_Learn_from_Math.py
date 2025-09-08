def solve(n):
    
    m = 9 if n%2 else 4
    
    return [m, n-m]

n = int(input())
print(*solve(n))