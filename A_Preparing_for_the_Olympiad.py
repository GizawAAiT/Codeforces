def solve(m, s, n):

    res = 0
    for idx in range(n-1):
        res += max(0, m[idx]- s[idx+1])

    res += m[-1]

    return res

for t in range(int(input())):
    n = int(input())
    m = [int(_inp) for _inp in input().strip().split()]
    s = [int(_inp) for _inp in input().strip().split()]

    print(solve(m, s, n))