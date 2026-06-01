def solve(n: int, a: list[int], b: list[int]) -> str:
    exact_diff, min_diff = -1, -1
    for ai, bi in zip(a, b):
        if bi > ai: return 'NO'
        diff = ai - bi
        if bi > 0:
            if exact_diff > -1 and diff != exact_diff:
                return 'NO'
            exact_diff = diff
        else:
            min_diff = max(min_diff, diff)
    
    if min_diff >-1 and exact_diff >-1 and min_diff > exact_diff:
        return 'NO'
    
    return 'YES'

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    print(solve(n, a, b))