def solve(n: int, s: int, r: int) -> list[int]:
    _max = s-r
    ans = [_max]
    n -= 1
    while n>0:
        val = min(r-n+1, _max)
        ans.append(val)
        
        r -= val
        n -= 1
    
    return ans

for t in range(int(input())):
    n, s, r = map(int, input().split())
    print(*solve(n, s, r))