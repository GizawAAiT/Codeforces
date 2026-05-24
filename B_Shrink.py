def solve(n: int) -> list[int]:
    ans = [0] * n
    l, r, val = 0, n-1, 1
    while l<r:
        ans[l] = val
        val += 1
        
        ans[r] = val
        val += 1
        
        l += 1
        r -= 1
    
    if l == r:
        ans[l] = val
    
    return ans

for t in range(int(input())):
    n = int(input())
    print(*solve(n))