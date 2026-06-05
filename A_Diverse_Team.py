def solve(n: int, k: int, a: list[int]) -> list[int]:
    _set = set()
    indices = []
    for idx, num in enumerate(a):
        if num not in _set:
            _set.add(num)
            indices.append(idx + 1)
        if len(_set) == k:
            return indices
    
    
    return False

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = [int(_) for _ in input().split()]
    ans = solve(n, k, a)
    if ans:
        print('YES')
        print(*ans)
    else:
        print('NO')