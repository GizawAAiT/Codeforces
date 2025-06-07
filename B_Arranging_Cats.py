from collections import defaultdict

def solve(s, f):
    cnt = defaultdict(int)
    for si, fi in zip(s, f):
        cnt[si+fi] += 1

    return max(cnt['10'], cnt['01'])

for _ in range(int(input())):
    n = int(input())
    s = input()
    f = input()
    print(solve(s, f))
