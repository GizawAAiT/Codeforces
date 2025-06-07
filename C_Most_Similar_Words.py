def solve(a, b):
    res = 0
    for ca, cb in zip(a, b):
        res += abs(ord(ca)-ord(cb))
    return res

for _ in range(int(input())):
    n, m = (int(_) for _ in input().split())
    words = []
    for _ in range(n):
        words.append(input().strip())
    
    _min = float('inf')
    for idx in range(n-1):
        for jdx in range(idx+1, n):
            _min = min(_min, solve(words[idx], words[jdx]))

    print(_min)
            