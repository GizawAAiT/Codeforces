def solve(n, m):
    res = []
    for row in range(n):
        if (row+1)%2 == 1:
            res.append('#'*m)
        
        elif (row+1) % 4 == 0:
            res.append('#' + '.'*(m-1))
        
        else:
            res.append('.'*(m-1) + '#')
    
    return res

n, m = (int(_) for _ in input().split())
res = solve(n, m)
for row in res:
    print(row)