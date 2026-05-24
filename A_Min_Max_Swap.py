def solve(n: int, a: list[int], b: list[int]) -> int:
    _max_a, _max_b = 0, 0
    for ai, bi in zip(a, b):
        _ai = min(ai, bi)
        _bi = max(ai, bi)
        
        _max_a = max(_max_a, _ai)
        _max_b = max(_max_b, _bi)
    
    return _max_a * _max_b

for t in range(int(input())):
    n = int(input())
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    print(solve(n, a, b))