def solve(arr: list[int], brr: list[int]):
    min_a, min_b = min(arr), min(brr)
    
    res = sum([max(a-min_a, b-min_b) for a, b in zip(arr, brr)])
    
    return res

for t in range(int(input())):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    brr = [int(_) for _ in input().split()]
    
    print(solve(arr, brr))
