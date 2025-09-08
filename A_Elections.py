def solve(cand):
    _max = [1, -float('inf')]
    for c in cand:
        if c > _max[1]:
            _max = [1, c]
        
        elif c == _max[1]:
            _max[0] += 1
    
    res = []
    for c in cand:
        if c == _max[1] and _max[0] == 1:
            res.append(0)
        else:
            res.append(_max[1]-c + 1)
    
    return res

for t in range(int(input())):
    cand = [int(_) for _ in input().split()]
    print(*solve(cand))