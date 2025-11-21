def solve(sides: list[int]) -> str:
    a, b, c, d = sorted(sides)
    if a != b or a != c or a != d:
        return "NO"
    
    return "YES"

for t in range(int(input())):
    sides = list(map(int, input().split()))
    print(solve(sides))