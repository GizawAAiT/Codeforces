def solve(n: int, k: int, arr: list[int]) -> int:
    
    num_zeros = 0
    ans = 0
    
    for x in arr:    
        if num_zeros == -1 or x == 0:
            num_zeros += 1
            
        if x == 1: 
            num_zeros = 0
            
        if num_zeros == k:
            ans += 1
            num_zeros = -1
    
    return ans

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(n, k, arr))