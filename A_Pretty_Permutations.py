def solve(n: int) -> list[int]:
    ans = []
    for idx in range(1, n+1, 2):
        if idx == n:
            ans.append(idx)
            ans[-1], ans[-2] = ans[-2], ans[-1]
        else:
            ans.append(idx+1)
            ans.append(idx)
    
    return ans

for t in range(int(input())):
    n = int(input())
    print(*solve(n))