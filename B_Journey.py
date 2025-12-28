def solve(n: int, a: int, b: int, c: int) -> int:
    _sum = a + b + c
    abc = n // _sum
    diff = n - _sum*abc
    
    if diff == 0:
        return 3 * abc
    
    if diff <= a:
        return 3 * abc + 1
    
    if diff <= a + b:
        return 3 * abc + 2
    
    return 3 * abc + 3

for t in range(int(input())):
    n, a, b, c = map(int, input().split())
    print(solve(n, a, b, c))