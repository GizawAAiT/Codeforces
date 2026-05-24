def solve(n: int, s: str) -> str:
    if n < 2 or s == '01' or s == '10':
        return 'YES'
    
    return 'NO'

for t in range(int(input())):
    n = int(input())
    s = input()
    print(solve(n, s))