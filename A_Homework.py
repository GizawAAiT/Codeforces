def solve(n: int, a: str, m: int, b: str, c: str) -> str:
    for bi, ci in zip(b, c):
        if ci == 'D':
            a = a + bi
        else:
            a = bi + a
    
    return a

for _ in range(int(input())):
    n = int(input())
    a = input().strip()
    m = int(input())
    b = input().strip()
    c = input().strip()
    print(solve(n, a, m, b, c))