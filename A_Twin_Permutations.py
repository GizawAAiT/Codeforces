def solve(n: int, nums) -> list[int]:
    return [n-num+1 for num in nums]

for t in range(int(input())):
    n = int(input())
    
    # permutation:
    nums = [int(_) for _ in input().split()]
    
    print(*solve(n, nums))