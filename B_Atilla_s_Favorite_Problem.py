def solve(s):
    _max = max(ord(char) for char in s)
    return _max - ord('a') + 1

for _ in range(int(input())):
    n = int(input())
    s = input()
    print(solve(s))
    