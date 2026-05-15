def solve(s: str, c: str) -> str:
    
    for i in range(len(s)):
        if s[i] == c and (i+1)%2:
            return 'YES'
        
    return 'NO'

for _ in range(int(input())):
    s = input().strip()
    c = input().strip()
    print(solve(s, c))