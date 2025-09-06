def solve(n, arr):
    if arr[0] + arr[1] <= arr[-1]:
        return [1,2,n]
    
    return [-1]

for t in range(int(input())):
    n = int(input())
    arr = [int(_) for _ in input().split()]
    
    print(*solve(n, arr))