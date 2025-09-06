def solve(rating):
    return 'HARD' if '1' in rating else 'EASY'

n = input()
rating = input().strip()
print(solve(rating))