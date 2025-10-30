def solve(nums):
    min_absolute = float('inf')
    
    for num in nums:
        min_absolute = min(min_absolute, abs(num))
    
    return min_absolute

if __name__ == '__main__':
    n = int(input())
    nums = [int(_) for _ in input().split()]
    
    print(solve(nums))