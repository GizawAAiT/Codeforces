def solve(n):
    perm = []
    for idx in range(n):
        if idx == 0:
            perm.append(n)
        else:
            perm.append(idx)
    
    print(*perm)
    
for t in range(int(input())):
    n = int(input())
    solve(n)