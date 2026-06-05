def solve(n: int, m: int, coordinates: list[tuple[int, int]]) -> int:
    x_total, y_total = 0, 0
    for idx in range(1, n):
        x_total += coordinates[idx][0]
        y_total += coordinates[idx][1]
    
    x_total += m
    y_total += m
    return 2 * (x_total + y_total)

for t in range(int(input())):
    n, m = map(int, input().split())
    coordinates = [tuple(map(int, input().split())) for _ in range(n)]
    print(solve(n, m, coordinates))