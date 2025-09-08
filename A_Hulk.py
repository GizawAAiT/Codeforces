def solve(n):
    feelings = []
    for i in range(n):
        feeling = 'hate'
        if i%2:
            feeling = 'love'
        suffix = 'it' if i == n-1 else 'that'
        feelings.append(f'I {feeling} {suffix}')
    
    return feelings

n = int(input())
print(*solve(n))