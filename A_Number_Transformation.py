def solve(x: int, y: int) -> list[int]:
    if y%x: return [0, 0]
    
    return [1, y//x]

for t in range(int(input())):
    x, y = map(int, input().split())
    print(*solve(x, y))