def solve(s: str) -> str:
    _mapping = {"L": "L", "R": "R", "U": 'D', "D": 'U'}
    
    ans = ''
    for c in s:
        ans += _mapping[c]
    
    return ans

for t in range(int(input())):
    n = input()
    s = input()
    print(solve(s))