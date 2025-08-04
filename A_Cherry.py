
def solve(arr, n):
    res = arr[0] * arr[1]
    for idx in range(1, n-1):
        res = max(res, arr[idx] * arr[idx+1])
    
    return res

for t in range(int(input())):
    n = int(input())
    arr = [int(__) for __ in input().split()]
    print(solve(arr, n))