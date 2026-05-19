def solve(n: int, a: list[int]) -> int:
    _min = min(a)
    _cnt = 0
    for num in a:
        _cnt += num > _min
    
    return _cnt

if __name__ == "__main__":
    for _t in range(int(input())):
        n = int(input())
        a = [int(_) for _ in input().strip().split()]
        print(solve(n, a))