def solve(nums):
    nums.sort()
    
    ans = []
    for idx in range(3):
        ans.append(nums[-1] - nums[idx])
        
    print(*ans
    )
    
if __name__ == '__main__':
    nums = [int(_) for _ in input().split()]
    solve(nums)