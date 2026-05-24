def solve(xA: int, yA: int, xB: int, yB: int, xF: int, yF: int) -> int:
    dist = abs(xB - xA) + abs(yB - yA)
    
    if (xA == xB == xF and yF >= min(yA, yB) and yF <= max(yA, yB)) or (
        yA == yB == yF and xF >= min(xA, xB) and xF <= max(xA, xB)):
        dist += 2
    
    return dist

for t in range(int(input())):
    input() # Empty input line
    
    xA, yA = map(int, input().split())
    xB, yB = map(int, input().split())
    xF, yF = map(int, input().split())
    
    print(solve(xA, yA, xB, yB, xF, yF))