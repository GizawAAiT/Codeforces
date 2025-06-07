def solve(arr, n):
    smashed = 0
    for idx in range(1, n):
        smashed += arr[idx]%2 - arr[idx-1]%2 == 0
        
    return smashed

for t in range(int(input())):
    n = int(input())
    arr = [int(__) for __ in input().strip().split()]
    print(solve(arr, n))