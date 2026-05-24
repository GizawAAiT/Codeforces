def solve(n: int) -> list[int]:
    
    ans = []
    for idx in range(n-1):
        if idx%2:
            ans.append(3)
        
        else: ans.append(-1)
    if n%2: ans.append(-1)
    else: ans.append(2)
    
    return ans

for t in range(int(input())):
    n = int(input())
    print(*solve(n))