def solve(n: int, strings: list[str]) -> str:
    # hash map for all unique characters accross all strings to their count.
    _map = {}
    for s in strings:
        for c in s:
            _map[c] = _map.get(c, 0) + 1
    
    for k, v in _map.items():
        if v%n: return "NO"
        
    return 'YES'

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        strings = []
        for _ in range(n):
            strings.append(input().strip())
        
        print(solve(n, strings=strings))