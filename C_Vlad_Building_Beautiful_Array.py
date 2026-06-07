def can_build_the_array(a: list[int]) -> str:
    _min_even, _min_odd = float('inf'), float('inf')
    
    for num in a:
        if num%2 == 0 and num < _min_even:
            _min_even = num

        if num%2 == 1 and num < _min_odd:
            _min_odd = num
    
    if _min_odd == float('inf') or _min_even == float('inf'): return "YES"
    
    if _min_odd < _min_even: return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(can_build_the_array(a))