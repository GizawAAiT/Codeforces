def solve(n: int, s: str) -> int:
    
    _set = set()
    for idx in range(1, n):
        melody = s[idx-1:idx+1]
        _set.add(melody)
    
    return len(_set)

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print(solve(n, s))