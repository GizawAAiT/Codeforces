def solve(x, k):
    if x%k == 0:
        return [x-1, 1]
    
    return [x]

for t in range(int(input())):
    x, k = (int(_) for _ in input().split())
    res = solve(x, k)
    
    # Outputs:
    print(len(res))
    print(*res)