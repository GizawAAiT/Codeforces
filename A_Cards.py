def solve(s: str) -> list[int]:
    ns, zs = s.count('n'), s.count('z')
    
    ans = []
    # Append 1's
    for _ in range(ns): ans.append(1)
    # Append 0's
    for _ in range(zs): ans.append(0)
    
    return ans

n = int(input())
s = input()
print(*solve(s))