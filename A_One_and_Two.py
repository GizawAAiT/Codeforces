def solve(n, nums):
    num_of_two = sum((num+1)%2 for num in nums)
    
    curr = 0
    for idx in range(n-1):
        curr += (nums[idx]+1)%2
        if curr == num_of_two/2:
            return idx + 1

    return -1

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(n, nums))