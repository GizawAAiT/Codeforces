def solve(n: int, k: int, x: int):
    if k == 1 or (k == 2 and x == 1 and n%2 == 1):
        return False
    
    if x != 1:
        return [1]*n
    
    # so, x is 1:
    if n%2 == 0:
        return [2]*(n//2)
    
    return [2]*(n//2 - 1) + [3]

for t in range(int(input())):
    n, k, x = (int(_) for _ in input().split())
    res = solve(n, k, x)
    if res:
        print('YES')
        print(len(res))
        print(*res)
    
    else:
        print('NO')