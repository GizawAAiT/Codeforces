def solve(n, k, arr):
    bud = 0
    count = 0
    
    for idx in range(n):
        if arr[idx]>=k: 
            bud += arr[idx]
        
        if arr[idx] == 0 and bud: 
            count += 1
            bud -= 1
        
    return count

for _ in range(int(input())):
    n, k = (int(_) for _ in input().split())
    arr = [int(_) for _ in input().split()]
    print(
        solve(n, k, arr)
    )
