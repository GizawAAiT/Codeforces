def solve(s: str) -> str:
    _cnt = {}
    
    for idx, val in enumerate(s):
        _cnt[val] = _cnt.get(val, 0) + 1
        
        if _cnt[val] > 1 and idx < len(s)-1: return "Yes"
    
    if _cnt[s[-1]] > 1 and s[-1] != s[0]: return "Yes"
    
    return "No"

for t in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s))