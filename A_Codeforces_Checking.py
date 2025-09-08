def solve(letter, pattern = 'codeforces'):
    return 'YES' if letter in pattern else 'NO'

for t in range(int(input())):
    letter = input().strip()
    print(solve(letter))