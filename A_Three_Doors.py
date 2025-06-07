def solve(arr, idx):
    for _ in range(2):
        if arr[idx-1] == 0: return "NO"
        idx = arr[idx-1]
    
    return "YES"
for _ in range(int(input())):
    idx = int(input())
    arr = [int(_) for _ in input().split()]
    print(solve(arr, idx))
