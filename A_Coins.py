def solve(n: int, k: int) -> int:
    if n%2 == 0 or k%2 == 1:
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n, k = (int(_) for _ in input().split())
    print(solve(n, k))