def solve(responses: list[tuple]):
    winner = (1, -1) # indx, quality
    for idx, resp in enumerate(responses):
        a, b = resp
        if a < 11 and b > winner[1]:
            winner = (idx + 1, b)
    
    print(winner[0])

for t in range(int(input())):
    n = int(input())
    responses = []
    for _ in range(n):
        a, b = (int(_) for _ in input().split())
        responses.append((a, b))
            
    solve(responses)