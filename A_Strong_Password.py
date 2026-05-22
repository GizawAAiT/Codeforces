def solve(s: str) -> str:
    if len(s) < 2:
        return s + 'a' if s!='a' else s+'b'
    
    s = list(s)
    for idx in range(len(s)-1):
        if s[idx] == s[idx + 1]:
            char = 'a' if s[idx] != 'a' else 'b'
            s.insert(idx+1, char)
            return ''.join(s)
    
    char = 'a' if s[-1] != 'a' else 'b'
    s.append(char)
    return ''.join(s)

for t in range(int(input())):
    s = input().strip()
    print(solve(s))