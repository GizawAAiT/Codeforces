def solve(nums: list[int], n: int):
    parity = [nums[0]%2, nums[1]%2]
    
    for idx in range(n):
        if nums[idx] % 2 != parity[idx % 2]:
            return "NO"
        
    return "YES"

for t in range(int(input())):
    n = int(input())
    print(solve(
        nums = [int(_) for _ in input().strip().split()],
        n = n
    ))