def solve(s: str, t: str) -> int:
    
    idx = 0
    while idx < min(len(s), len(t)) and s[idx] == t[idx]:
        idx += 1
    
    return len(s) + len(t) - idx + 1 if idx > 0 else len(s) + len(t)

for _ in range(int(input())):
    s = input()
    t = input()
    print(solve(s, t))