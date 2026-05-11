def solve(n: int, arr: list[int]) -> int:
    _max = max(arr)
    
    return _max * n

for _ in range(int(input())): 
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(n, arr))