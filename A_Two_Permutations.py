def solve(n: int, a: int, b: int) -> str:
    
    if n-(a+b) > 1 or a == b == n:
        return 'Yes'
    
    return 'No'

for _t in range(int(input())):
    n, a, b = map(int, input().split())
    print(solve(n, a, b))