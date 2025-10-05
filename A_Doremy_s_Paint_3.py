def solve(nums):
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    if len(frequency.keys()) > 2:
        return 'No'
    
    if len(frequency.keys()) == 1: return 'Yes'
    
    a, b = tuple(frequency.keys())
    if max(frequency[a], frequency[b]) > min(frequency[a], frequency[b]) + 1:
        return 'No'
    return 'Yes'

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(nums))