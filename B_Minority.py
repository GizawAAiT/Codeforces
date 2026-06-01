from collections import Counter

def solve(s: str) -> int:
    cnt = Counter(s)
    # give default zero value if any of the keys (0, 1) doesn't exist:
    cnt['0'] = cnt.get('0', 0)
    cnt['1'] = cnt.get('1', 0)
    
    _min_cnt, _max_cnt = min(cnt.values()), max(cnt.values())
    return _min_cnt if _min_cnt < _max_cnt else _min_cnt - 1

for t in range(int(input())):
    s = input()
    print(solve(s))