def solve(n, nums):
    total = sum(nums)
    av = total/n
    
    running_sum = 0
    for idx, num in enumerate(nums):
        running_sum += num
        if running_sum/(idx+1) < av: 
            return "NO"
        
    return "YES"

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(n, nums))