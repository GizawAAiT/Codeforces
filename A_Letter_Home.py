def solve(xs: list[int], s: int) -> int:
    
    _min, _max = min(xs), max(xs)
    
    if _min < s < _max:
        path1 = abs(s-_min) + abs(_max-_min)
        path2 = abs(s-_max) + abs(_max-_min)
        
        return min(path1, path2)
    
    else:
        return max(abs(s-_min), abs(s-_max))

for _ in range(int(input())):
    n, s = map(int, input().split())
    xs = list(map(int, input().split()))
    print(solve(xs, s))