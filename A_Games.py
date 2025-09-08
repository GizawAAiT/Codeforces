from collections import defaultdict
def solve(uniforms):
    guests = defaultdict(int)
    for _, g in uniforms:
        guests[g] += 1
    
    res = 0
    for h, _ in uniforms:
        res += guests[h]
    
    print(res)
    
n = int(input())
uniforms = []
for _ in range(n):
    h, g = (int(_) for _ in input().split())
    uniforms.append((h, g))
    
solve(uniforms)