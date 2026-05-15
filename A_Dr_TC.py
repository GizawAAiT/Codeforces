from collections import Counter

def solve(n: int, _binary: str) -> int:
    
    _cnt_1 = Counter(_binary)['1']
    res = 0
    for bit in _binary:
        if bit == '1':
            res += _cnt_1 - 1
        else: res += _cnt_1 + 1
    
    return res

for _ in range(int(input())):
    n = int(input())
    _binary = input().strip()
    print(solve(n, _binary))