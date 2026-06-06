def too_min_too_max_absolute_difference_sum(n: int, a: list[int]) -> int:
    
    _min, _2nd_min, _max, _2nd_max = (
        float('inf'), float('inf'), float('-inf'), float('-inf'))
    
    for num in a:
        if num < _min:
            _2nd_min = _min
            _min = num
        elif num < _2nd_min:
            _2nd_min = num
        
        if num > _max:
            _2nd_max = _max
            _max = num
        elif num > _2nd_max:
            _2nd_max = num
    
    d1, d2, d3 = _max - _2nd_max, _2nd_max - _2nd_min, _2nd_min - _min
    return 2*(d1+d3) + 4*d2

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        a = [int(_) for _ in input().split()]
        print(too_min_too_max_absolute_difference_sum(n, a))