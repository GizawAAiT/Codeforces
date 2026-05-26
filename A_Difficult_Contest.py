def solve(s: str) -> str:
    ts = ''.join([cr for cr in s if cr == 'T'])
    
    others = ''.join([cr for cr in s if cr != 'T'])
    
    return ts + others

for t in range(int(input())):
    s = input()
    print(solve(s))