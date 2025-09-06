def solve(n, accom):
    total = 0
    for p, q in accom:
        total += (q-p > 1)
    
    return total

n = int(input())
accom = []
for _ in range(n):
    p, q = (int(_) for _ in input().split())
    accom.append((p, q))

print(solve(n, accom))
