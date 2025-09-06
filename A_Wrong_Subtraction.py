def solve(n, k):
    for _ in range(k):
        if n%10:
            n -= 1
        else:
            n //=10
            
    return n

n, k = (int(_) for _ in input().split())
print(solve(n, k))