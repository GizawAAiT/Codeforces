from collections import defaultdict
def solve(nums):
    cnt = defaultdict(int)
    for idx in range(3):
        cnt[nums[idx]] += 1
    
    repeated = None
    for k in cnt.keys():
        if cnt[k] > 1: 
            repeated = k
    
    for idx, num in enumerate(nums):
        if num != repeated:
            return idx+1

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(nums))