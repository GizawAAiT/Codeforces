def solve(a, b, c):
    if max(a,b) < c or max(a,c) < b or max(b,c) < a or len(set([a,b,c])) == 3:
        return False
    
    return [a,  b, c]

for t in range(int(input())):
    a, b, c = (int(_) for _ in input().split())
    res = solve(a, b, c)
    if res:
        print('YES')
        print(*res)
    
    else: print('NO')
    
    