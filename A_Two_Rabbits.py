def solve(x: int, y: int, a: int, b: int) -> int:
    distance = y-x
    jump = a + b
    return distance//jump if distance % jump == 0 else -1

for t in range(int(input())):
    x, y, a, b = map(int, input().split())
    print(solve(x, y, a, b))