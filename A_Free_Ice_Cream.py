def solve(n, x, reqs):
    
    distress = 0
    for req in reqs:
        if req < 0 and abs(req) > x:
            distress += 1
        else:
            x += req

    print(f'{x} {distress}')

n, x = (int(_) for _ in input().split())
reqs = []
for _ in range(n):
    sign, val = (_ for _ in input().split())
    if sign == '+':
        reqs.append(int(val))
    else:
        reqs.append(-int(val))

solve(n, x, reqs)