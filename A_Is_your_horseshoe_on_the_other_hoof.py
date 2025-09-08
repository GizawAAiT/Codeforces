def solve(colors):
    return 4-len(set(colors))

colors = input().split()
print(solve(colors))