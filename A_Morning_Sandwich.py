def solve(b: int, c: int, h: int) -> int:
    pairs = min(b-1, c + h)
    return 2*pairs + 1

for t in range(int(input())):
    b, c, h = map(int, input().split())
    
    print(solve(b, c, h))