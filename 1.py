def solve(s: str) -> int:
    _map, count = {}, 0
    for c in s:
        _map[c] = _map.get(c, 0) + 1
        count += _map[c] < 3
        
    return count //2

for t in range(int(input())):
    s = input()
    print(solve(s))