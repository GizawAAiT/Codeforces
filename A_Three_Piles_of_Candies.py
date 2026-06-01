def solve(a: int, b: int, c: int) -> int:
    return (a + b + c)//2

for q in range(int(input())):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))