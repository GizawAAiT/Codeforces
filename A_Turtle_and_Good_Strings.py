solve = lambda x: x[0] != x[-1]

for _ in range(int(input())): # Test cases
    input() # n!
    print("YES" if solve(input()) else "NO")