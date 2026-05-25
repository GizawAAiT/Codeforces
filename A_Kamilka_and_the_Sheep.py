def solve(n: int, a: list[int]) -> int:
    _min, _max = float('inf'), -float('inf')
    for num in a:
        _min = min(_min, num)
        _max = max(_max, num)
    
    increment = _max - 2 * _min
    return _min + increment

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    print(solve(n, a))