def solve(nums, dig):

    insertion_indx = len(nums)
    for idx, num in enumerate(nums):
        
        if dig > num:
            insertion_indx = idx
            break

    nums.insert(insertion_indx, dig)
    return "".join(nums)

for _ in range(int(input())):
    n, d = (input().strip().split())
    nums = list(input().strip())
    print(solve(nums, d))
