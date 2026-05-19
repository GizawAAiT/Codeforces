def solve(n: int, nums: list[int]) -> list[int]:
    """
    Given n integers, return deduplicated list keeping the last occurrence of 
    each integer.
    Args:
        n (int): number of integers
        nums (list[int]): list of integers
    
    Returns: 
        list[int]: deduplicated list of integers
    """
    
    # keep a set:
    _seen = set()
    
    # Traverse backward. Mark repeated as -1:
    for i in range(n-1, -1, -1):
        if nums[i] in _seen:
            nums[i] = -1
        else:
            _seen.add(nums[i])
    
    # return deduplicated (those not marked as -1):
    return [num for num in nums if num != -1]

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    res = solve(n, nums)
    print(len(res))
    print(*res)