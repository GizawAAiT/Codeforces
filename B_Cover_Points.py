def solve(sides):
    res = 0
    for x, y in sides:
        res = max(res, x+y)
        
    return res

sides = []
for _ in range (int(input())):
    side = (int(_) for _ in input().split())
    sides.append(side)
# print(sides)
print(solve(sides))