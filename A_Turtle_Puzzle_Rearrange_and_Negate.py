def calc_max_sum(nums: list[int]):
    return sum(abs(num) for num in nums)


for _ in range(int(input())):
    n = input()
    nums = [int(_) for _ in input().split()]
    print(calc_max_sum(nums))