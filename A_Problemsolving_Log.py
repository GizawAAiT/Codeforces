def solve(n: int, s: str) -> int:
    
    # hashmap (keys are capital letters, values their distance from "A")
    _map = {chr(i): i-64 for i in range(65, 97)}
    
    ans = 0
    
    for c in s:
        _map[c] -= 1
        if _map[c] == 0:
            ans += 1
    
    return ans

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print(solve(n, s))