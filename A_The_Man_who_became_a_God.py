import heapq
def solve(n: int, k: int, nums: list[int]):
    # Its always guaranteed that k<=n
    total_power, top_k = 0, []
    
    for idx in range(1, n):
        val = abs(nums[idx]-nums[idx-1])
        
        heapq.heappush(top_k, val)
        
        if len(top_k) > k-1:
            heapq.heappop(top_k)
        
        total_power += val
    
    return total_power - sum(top_k)

for t in range(int(input())):
    n, k = (int(_) for _ in input().split())
    nums = [int(_) for _ in input().split()]
    print(solve(n, k, nums))