def solve(nums):
    prev = nums[0]
    
    for num in nums[1:]:
        if abs(num-prev) not in [5, 7]:
            return "NO"
        
        prev = num
    
    return "YES"

for t in range(int(input())):
    
    n = int(input())
    nums = [int(_) for _ in input().split()]
    
    print(solve(nums))