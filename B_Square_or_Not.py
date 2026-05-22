from math import sqrt

def solve(s: str) -> str:
    boxes = len(s)
    if sqrt(boxes) != int(sqrt(boxes)):
        return 'No'
    
    side = sqrt(boxes)
    ones = 4*side - 4
    
    return 'Yes' if ones == s.count('1') else 'No'

for t in range(int(input())):
    n = int(input())
    s = input().strip()
    print(solve(s))