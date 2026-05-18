def solve(k: int, x: int) -> int:
    
    n = 1
    while k:
        n += x
        k -= 1
    
    return n

for _ in range(int(input())):
    k, x = map(int, input().strip().split())
    print(solve(k, x))