def solve(pattern: str, base: str = 'codeforces'):
    cnt = 0
    for idx in range(len(base)):
        cnt += pattern[idx] != base[idx]
    
    return cnt

for t in range(int(input())):
    pattern = input().strip()
    print(solve(pattern))