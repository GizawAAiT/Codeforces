def solve(xs):
    return (max(xs) - min(xs))**2

for t in range(int(input())):
    xs = []
    for _ in range(4):
        x, y = (int(_) for _ in input().strip().split())
        xs.append(x)

    print(solve(xs))