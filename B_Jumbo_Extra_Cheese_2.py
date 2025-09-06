def solve(sides, n):
    sides.sort(reverse=True)
    total = 0
    for idx in range(n-1):
        l1, w1= sides[idx]
        l2, w2 = sides[idx+1]
        
        total += 2*(l1+w1)-2*l2
    
    l, w = sides[-1]
    total += 2*(l+w)
    # print(f'sides: {sides}')
    return total

for t in range(int(input())):
    n = int(input())
    sides = []
    for _ in range(n):
        l, w = (int(_) for _ in input().split())
        sides.append((max(l, w), min(l, w)))
    print(solve(sides, n))
