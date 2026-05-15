def solve(n: int, s: str) -> str:
    
    a = ''
    
    l, r = 0, 1
    while l<n and r<n:
        
        if s[l] != s[r]:
            r += 1
        
        else:
            a += s[l]
            l = r + 1
            r = l + 1
    
    return a

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(n, s))