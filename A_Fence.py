def solve(sides):
    
    return sum(sides)-1

for t in range(int(input())):
    sides = [int(_) for _ in input().split()]
    print(solve(sides))