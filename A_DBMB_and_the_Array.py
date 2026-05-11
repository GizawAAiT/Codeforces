def solve(n: int, s: int, x: int, a: list[int]) -> str:
    total = sum(a)
    
    diff = s - total
    if diff >= 0 and diff % x == 0:
        return 'YES'
    
    return 'NO'

for _ in range(int(input())):
    n, s, x = map(int, input().split())
    
    a = list(map(int, input().split()))
    print(solve(n, s, x, a))

