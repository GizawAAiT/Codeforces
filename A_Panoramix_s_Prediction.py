from math import sqrt

def solve(n: int, m: int):
    for num in range(n+1, m):
        if is_prime(num):
            return 'NO'
    
    return 'YES' if is_prime(m) else 'NO'

def is_prime(num):
    if num < 2: return False
    
    if num == 2: return True
    
    if num%2 == 0: return False
    
    for _ in range(3, int(sqrt(num))+1, 2):
        if num%_ == 0: return False
    
    return True

n, m = (int(_) for _ in input().split())
print(solve(n, m))