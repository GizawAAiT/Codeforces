def solve(n: int, k: int) -> str:
    
    ans = ''
    for _ in range(n):
        for base_ord in range(k):
            ans += chr(base_ord + 97)
    
    return ans

for t in range(int(input())):
    n, k = map(int, input().split())
    print(solve(n, k))