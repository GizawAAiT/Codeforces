def solve(s: str) -> str:
    base = 'Yes'
    s_idx, base_idx = 0, 0
    while base_idx < 3 and base[base_idx] != s[0]:
        base_idx += 1
    
    while s_idx < len(s):
        base_idx %= 3
        if s[s_idx] != base[base_idx]: return 'NO'
        s_idx += 1
        base_idx += 1
    
    return 'YES'

for t in range(int(input())):
    s = input()
    print(solve(s))