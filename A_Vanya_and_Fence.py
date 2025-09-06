def solve(n, h, arr):
    bent = 0
    for a in arr:
        if a > h: bent += 1
    
    return n + bent

n, h = (int(_) for _ in input().split())
arr = [int(_) for _ in input().split()]
print(solve(n, h, arr))