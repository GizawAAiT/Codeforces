def solve(s: str) -> int:
    _cnt = 0
    
    _set = set()
    for c in s:
        _set.add(c)
        if len(_set) > 3:
            _cnt += 1
            _set.clear()
            _set.add(c)
        
    if len(_set) > 0: _cnt += 1
    
    return _cnt

for n in range(int(input())):
    s = input()
    print(solve(s))