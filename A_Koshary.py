def can_reach_the_XY_coordinates(x: int, y: int) -> str: #YES, NO
    
    return "YES" if x % 2 + y % 2 < 2 else "NO"

for t in range(int(input())):
    x, y = map(int, input().split())
    print(can_reach_the_XY_coordinates(x, y))