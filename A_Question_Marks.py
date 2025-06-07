from collections import defaultdict

def solve(s, n):
    cnt = defaultdict(int)
    for ch in s:
        cnt[ch] += 1

    _max_cnt_per_ans, res = n, 0

    for ch in ["A", "B", "C", "D"]:
        res += min(cnt[ch], _max_cnt_per_ans)
    
    return res

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print(solve(s, n))



