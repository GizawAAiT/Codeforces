def solve(s: str) -> int:
    return s.count('1')

for t in range(int(input())):
    s = input()
    print(solve(s))