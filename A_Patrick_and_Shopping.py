def solve(d1: int, d2: int, d3: int) -> int:
    path_1 = 2 * (d1 + d2)
    path_2 = d1 + d2 + d3
    path_3 = 2 * (d1 + d3)
    path_4 = 2 * (d2 + d3)
    
    return min(path_1, path_2, path_3, path_4)

d1, d2, d3 = map(int, input().split())
print(solve(d1, d2, d3))