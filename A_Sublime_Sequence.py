def solve(x: int, n: int)-> int:
    if n % 2:
        return x
    
    return 0

for _ in range(int(input())):
    x, n = (int(_) for _ in input().strip().split())
    print(solve(x, n))