def solve(arr):
    _mx, mx_idx = 0, 0
    for idx, val in enumerate(arr):
        if arr[idx] > arr[mx_idx]:
            _mx = val
            mx_idx = idx
    
    res = 0
    for idx, val in enumerate(arr):
        if idx != mx_idx:
            res += 2*val-1
    
    return res

for _ in range(int(input())):
    n, k = (int(_) for _ in input().split())
    arr = [int(_) for _ in input().split()]
    print(solve(arr))




