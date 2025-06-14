def solve(s):
    dic = {}
    for idx in range(len(s)):
        parity = idx%2
        if s[idx] not in dic:
            dic[s[idx]] = parity

        elif dic[s[idx]] != parity:
            return "NO" 

    return "YES"

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s))