def solve(r: int, b: int, d: int) -> str:
    _min, _max = min(r, b), max(r, b)
    return 'YES' if (_max - 1)// _min <= d else 'NO'

if __name__ == "__main__":
    for t in range(int(input())):
        r, b, d = map(int, input().split())
        
        print(solve(r, b, d))