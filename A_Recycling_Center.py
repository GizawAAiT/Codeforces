def solve(n: int, c: int, a: list[int]) -> int:
    destroyed_by_zero_power = 0
    
    # sort the array a:
    a.sort()
    idx = n-1
    while idx > -1:
        if a[idx] <= c: 
            destroyed_by_zero_power += 1
            c /= 2
        
        idx -= 1
    
    return n - destroyed_by_zero_power

for t in range(int(input())):
    n, c = map(int, input().split())
    a = [int(_) for _ in input().split()]
    print(solve(n, c, a))