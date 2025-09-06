def solve(n):
    INF = 10**4
    
    layer = 0
    for h in range(INF):
        layer += (h+1)
        n -= layer
        
        if n < 0:
            return h
    
n = int(input())
print(solve(n))