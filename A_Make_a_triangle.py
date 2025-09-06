def solve(sides):
    sides.sort()
    
    l1, l2, l3 = sides[0], sides[1], sides[2]
    
    return max(0, l3+1-l1-l2)

sides = [int(_) for _ in input().split()]
print(solve(sides))
    