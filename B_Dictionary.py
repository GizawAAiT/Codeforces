def solve(s: str) -> int:
    complete = ord(s[0]) - 97 # 97 is ord('a')
    curr = ord(s[1]) - 97 if s[1] > s[0] else ord(s[1]) - 96
    
    return complete * 25 + curr

for t in range(int(input())):
    s = input()
    print(solve(s))