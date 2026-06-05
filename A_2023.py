from math import prod
def solve(n: int, k: int, b: list[int]) -> int:
    
    removed = 2023 / prod(b)
    if int(removed) < removed:
        return False
    
    ans = [int(removed)]
    for _ in range(k-1):
        ans.append(1)
    
    return ans

for t in range(int(input())):
    n, k = map(int, input().split())
    b = [int(_) for _ in input().split()]
    ans = solve(n, k, b)
    if ans:
        print('YES')
        print(*ans)
    else:
        print('NO')