def solve(perm):
    if min(perm) != perm[0]:
        return 'NO'
    
    return 'YES'

for t in range(int(input())):
    n = input()
    perm = [int(_) for _ in input().split()]
    print(solve(perm))