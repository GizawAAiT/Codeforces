def solve(s: str, t: str):
    
    if s == t[::-1]:
        return 'YES'
    
    return 'NO'

s = input()
t = input()
print(solve(s, t))