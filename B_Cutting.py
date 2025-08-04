# def solve(n: int, B: int, nums: list[int]):
#     dic = {0:0, 1:0}
    
#     costs = []
#     for idx, num in enumerate(nums):
#         dic[num%2] += 1
        
#         if dic[1] == dic[0] and idx < n-1:
#             costs.append(abs(nums[idx]-nums[idx+1]))
    
#     costs.sort()
#     idx = 0
#     while idx < len(costs) and B-costs[idx]>=0:
#         B -= costs[idx]
#         idx += 1
    
#     return idx
def max_cuts_bucket(n: int, B: int, a: list[int]) -> int:
    # bucket[c] = how many legal cuts have cost c
    bucket = [0] * 101        # indices 0…100, we’ll use 1…99/100

    odd = even = 0
    for i in range(n - 1):
        if a[i] & 1:
            odd += 1
        else:
            even += 1
        if odd == even:       # legal cut just after a[i]
            cost = abs(a[i] - a[i + 1])
            if cost <= B:     # costs > B can never be chosen
                bucket[cost] += 1
    
    cuts = 0
    remaining = B
    for cost in range(1, B + 1):       # ascending cost order
        if bucket[cost]:
            max_take = min(bucket[cost], remaining // cost)
            cuts      += max_take
            remaining -= max_take * cost
            if remaining == 0:
                break
    return cuts


n, B = (int(_) for _ in input().split())
nums = [int(_) for _ in input().split()]
print(max_cuts_bucket(n, B, nums))