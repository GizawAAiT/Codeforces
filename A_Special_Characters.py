def solve(n: int) -> str:
    if n%2: return False
    
    ans = ''
    for idx in range(n//2):
        if idx%2:
            ans += 'AA'
        else:
            ans += 'BB'
    
    return ans

for t in range(int(input())):
    n = int(input())
    sol_ = solve(n)
    if not sol_:
        print('NO')
    else:
        print('YES')
        print(sol_)