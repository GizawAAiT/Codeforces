def solve(initial):
    l, d = initial[0], initial[1]
    
    res = []
    for i in range(1, 9):
        if int(d) != i:
            res.append(l + str(i))
    
    for chr in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        if chr != l:
            res.append(chr + d)
    
    return res
    
for t in range(int(input())):
    initial = input()
    res = solve(initial)
    for r in res:
        print(r)