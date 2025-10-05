def solve(nums):
    even_count, odd_count = 0, 0
    for num in nums:
        even_count += num % 2 == 0
        odd_count += num % 2
        
    
    return 'Yes' if even_count == odd_count else 'No'

for t in range(int(input())):
    n = input()
    nums = [int(_) for _ in input().split()]
    print(solve(nums))