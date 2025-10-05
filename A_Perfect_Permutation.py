def solve(n):
    if n % 2: return [-1]
    perm = [i+2 if i%2==0 else i for i in range(n)]
    
    perm[0], perm[1] = 2, 1
    
    return perm

n = int(input())
print(*solve(n))