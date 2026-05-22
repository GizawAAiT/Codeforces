def solve(n: int, a: list[int]) -> int:
    _map = {}
    for num in a:
        _map[num] = _map.get(num, 0) + 1
    
    ans, _min = -1, float('inf')
    for idx, v in enumerate(a):
        if _map[v] == 1 and v < _min:
            ans = idx + 1
            _min = v
    
    return ans

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        a = [int(_) for _ in input().split()]
    
        print(solve(n, a))