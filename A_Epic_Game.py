def gcd(a: int,  b: int) -> int:
    while b:
        a, b = b, a%b
    
    return a

def solve(a: int, b: int, n: int) -> str:
    ans = ['1', '0']
    candidates = [a, b]
    idx = 0
    while n>0:
        n -= gcd(n, candidates[idx])
        idx = (idx + 1)%2
    
    return ans[idx]

a, b, n = map(int, input().split())
print(solve(a, b, n))