def second_min(nums: list[int]) -> int:
    
    _min, _2nd_min = float('inf'), float('inf')
    
    for num in nums:
        if num < _min:
            _2nd_min = _min
            _min = num
            
        elif _min < num < _2nd_min:
            _2nd_min = num
    
    return _2nd_min if _2nd_min != float('inf') else 'NO'

if __name__ == "__main__":
    n = int(input())
    nums = [int(_) for _ in input().split()]
    print(second_min(nums))