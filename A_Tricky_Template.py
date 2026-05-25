def solve(a: str, b: str, c: str) -> str:
    for ai, bi, ci in zip(a, b, c):
        if ai != ci and bi != ci:
            return 'YES'
        
    return 'NO'

for t in range(int(input())):
    n = int(input())
    a, b, c = input(), input(), input()
    print(solve(a, b, c))