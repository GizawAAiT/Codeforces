def solve(points: list[int]):
    return max(points) - min(points)

for t in range(int(input())):
    points = [int(__) for __ in input().split()]
    print(solve(points))