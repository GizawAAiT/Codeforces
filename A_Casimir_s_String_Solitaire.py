from collections import defaultdict

def solve(inp):
    cnt = defaultdict(int)
    for i in inp:
        cnt[i] += 1
    
    if cnt['A'] + cnt['C'] == cnt['B']:
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    inp = input()
    print(solve(inp))