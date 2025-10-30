def solve(nums):
    a3s = [nums[0] + nums[1], nums[2]-nums[1]]
    
    result = []
    for a3 in a3s:
        res = 0
        if nums[0] + nums[1] == a3:
            res += 1
        if nums[1] + a3 == nums[2]:
            res += 1
        if a3 + nums[2] == nums[3]:
            res += 1
        
        result.append(res)
    
    return max(result)

for t in range(int(input())):
    nums = [int(_) for _ in input().split()]
    
    print(solve(nums))