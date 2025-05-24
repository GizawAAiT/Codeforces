def is_non_decreasing(arr):
    for idx in range(1, len(arr)):
        if arr[idx] < arr[idx-1]: return False
    
    return True

def solve(arr, n, k):
    if 1<k:
        return True
    
    return is_non_decreasing(arr)

for _ in range(int(input())):
    n, k = (int(_) for _ in input().split())
    arr = [int(_) for _ in input().split()]
    print("YES" if solve(arr, n, k) else "NO")