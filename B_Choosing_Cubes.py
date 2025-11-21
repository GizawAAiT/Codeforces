def solve(n: int, f: int, k: int, a: list[int]) -> str:
    reference = a[f-1]
    greater_than_f, greater_or_equal_f = 0, 0
    for ai in a:
        greater_than_f += ai > reference
        greater_or_equal_f += ai >= reference
    
    # we remove the largest k cubes and if the reference removed, return "YES":
    if greater_or_equal_f <= k:
        return 'YES'
    
    if greater_than_f >= k:
        return 'NO'
    
    return "MAYBE"
    
for t in range(int(input())):
    n, f, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, f, k, a))