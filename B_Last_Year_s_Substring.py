def solve(n: int, s: str) -> str:
    pattern = '2020'
    
    l, r = 0, -1
    
    while l < 4 and s[:l+1] == pattern[:l+1]:
        l += 1
    
    while -r <= 4 and s[r:] == pattern[r:]:
        r -= 1
        
    return 'YES' if l - r - 1 >= 4 else 'NO'

for t in range(int(input())):
    n = int(input())
    s = input()
    print(solve(n, s))