def dimen(d: int):
    if d%2: return 1 # base case
    
    return dimen(d//2) * 2

def solve(w, h, n):
    tot = dimen(w) * dimen(h)
    return 'YES' if tot >= n else "NO"

for t in range(int(input())):
    w, h, n = (int(_) for _ in input().split())
    print(solve(w, h, n))
        