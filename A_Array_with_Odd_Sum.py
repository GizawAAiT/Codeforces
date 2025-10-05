def solve(n, nums):
    even_count = odd_count = 0
    for num in nums:
        even_count += (num+1)%2
        odd_count += num%2
    
    if n == even_count or (n == odd_count and n %2 == 0):
        return 'NO'
    
    return 'YES'

for t in range(int(input())):
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(solve(n, nums))