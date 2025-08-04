from collections import deque

def min_jump_bruteforce(s: str) -> int:
    n = len(s)
    for d in range(1, n + 2):                     # n+1 is certainly enough
        vis = [False]*(n+2)
        q = deque([0])
        vis[0] = True
        while q:
            i = q.popleft()
            if i == n + 1:
                return d
            if i == 0 or s[i-1] == 'R':           # move right
                for nxt in range(i+1, min(n+2, i+d+1)):
                    if not vis[nxt]:
                        vis[nxt] = True
                        q.append(nxt)
            if i and s[i-1] == 'L':               # move left
                for nxt in range(max(0, i-d), i):
                    if not vis[nxt]:
                        vis[nxt] = True
                        q.append(nxt)
    return n + 1


for t in range(int(input())):
    s = s = input().strip()
    print(min_jump_bruteforce(s))