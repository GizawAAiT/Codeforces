def solve(games: list[tuple[int]]):
    m_cnt = c_cnt = 0
    for m, c in games:
        m_cnt += m>c
        c_cnt += c>m
        
    if m_cnt > c_cnt:
        return 'Mishka'
    
    elif c_cnt>m_cnt:
        return 'Chris'
    
    return 'Friendship is magic!^^'

n = int(input())
games = []
for _ in range(n):
    games.append((int(_) for _ in input().split()))
    
print(solve(games))