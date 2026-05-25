def solve(s: list[str]) -> str:
    _map = ["OOO", "XXX", "+++"]
    # Horizontal:
    for row in s:
        if row in _map:
            return row[0]
    
    #: Vertical:
    for col in range(3):
        path = s[0][col] + s[1][col] + s[2][col]
        if path in _map:
            return path[0]
    
    #: Diagonal
    diagonal1 = s[0][0] + s[1][1] + s[2][2]
    if diagonal1 in _map:
        return diagonal1[0]
    
    diagonal2 = s[0][2] + s[1][1] + s[2][0]
    if diagonal2 in _map:
        return diagonal2[0]
    
    return "DRAW"

for t in range(int(input())):
    s = []
    for _ in range(3):
        s.append(input().strip())
    print(solve(s))