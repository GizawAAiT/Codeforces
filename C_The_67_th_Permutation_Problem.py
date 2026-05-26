def solve(n: int) -> list[int]:
    ans = []
    for group in range(n):
        i, j, k = group + 1, (n+1) + 2 * group, (n+2) + 2*group
    
        ans.extend([i, j, k])
    
    return ans

for t in range(int(input())):
    n = int(input())
    print(*solve(n))