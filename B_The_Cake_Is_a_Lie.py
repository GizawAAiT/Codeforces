from functools import lru_cache
def solve(n, m, k):
    def is_bounded(x, y):
        return 1 <= x <= m and 1 <= y <= n
    
    @lru_cache(None)
    def dfs(x, y, cost):
        if not is_bounded(x, y):
            return False

        if x == m and y == n:
            return cost == k
        
        return dfs(x+1, y, cost + y) or dfs(x, y+1, cost + x)
    
    return 'YES' if dfs(1,1,0) else 'NO'

for t in range(int(input())):
    n, m, k = (int(_) for _ in input().split())
    print(solve(n, m, k))