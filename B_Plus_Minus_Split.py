from collections import defaultdict

def solve(s):
    cnt = defaultdict(int)
    for ch in s:
        cnt[ch] += 1
    
    return abs(cnt["+"] - cnt["-"])
for _ in range(int(input())):
    input() # n!
    print(solve(input())) # s!