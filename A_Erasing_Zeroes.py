def solve(s: str) -> int:
    
    l, r, ans = 0, len(s)-1, 0
    
    while l < len(s) and s[l] == '0':
        l += 1
    
    while r >= 0 and s[r] == '0':
        r -= 1
    
    for idx in range(l, r):
        ans += s[idx] == '0'
    
    return ans

for _testcases in range(int(input())):
    s = input().strip()
    print(solve(s))