def solve(n: int, j: int, k: int, arr: list[int]) -> str:
    
    _max = max(arr)
    
    if k == 1 and arr[j-1] != _max:
        return 'NO'
    
    return 'YES'

for _ in range(int(input())):
    n, j, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, j, k, arr))