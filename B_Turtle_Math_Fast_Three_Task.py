def solve(n: int, nums: list[int]):
    MOD = sum(nums) % 3
    if MOD == 0: return 0
    if MOD == 2: return 1
    
    for num in nums:
        if num%3 == MOD: return 1
    
    return 2

for t in range(int(input())):
    n = int(input())
    print(solve(n=n, 
                nums=[int(_) for _ in input().strip().split()]))