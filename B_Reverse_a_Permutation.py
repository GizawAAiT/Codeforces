def solve(n: int, p: list[int]) -> list[int]:
    
    l = 0
    while l < n and p[l] == n - l:
        l += 1
    
    r = n-1
    while r > l and p[r] != n-l:
        r -= 1
    
    # flip the subarray from l to r:
    while l < r:
        p[l], p[r] = p[r], p[l]
        l += 1
        r -= 1
    
    return p

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    print(*solve(n, p))