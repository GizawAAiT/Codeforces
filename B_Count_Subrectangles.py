import math, sys

def count_len(runs, L):
    """number of sub-segments of length L inside the list of run lengths"""
    return sum(r - L + 1 for r in runs if r >= L)

def count_subrectangles_fast(a, b, k):
    n, m = len(a), len(b)

    # gather run lengths
    runsA, runsB = [], []
    cur = 0
    for v in a:
        if v: cur += 1
        else:
            if cur: runsA.append(cur)
            cur = 0
    if cur: runsA.append(cur)

    cur = 0
    for v in b:
        if v: cur += 1
        else:
            if cur: runsB.append(cur)
            cur = 0
    if cur: runsB.append(cur)

    ans = 0
    for x in range(1, int(math.isqrt(k)) + 1):
        if k % x == 0:
            y = k // x
            ans += count_len(runsA, x) * count_len(runsB, y)
            if x != y:                       # complementary dimensions
                ans += count_len(runsA, y) * count_len(runsB, x)
    return ans

n, m, k = (int(_) for _ in input().split())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
print(count_subrectangles_fast(a, b, k))