def solve(n: int, a: str, b: str) -> int:
    
    res = 0
    
    for idx in range(n):
        diff = abs(int(a[idx]) - int(b[idx]))
        res += min (diff, 10 - diff)
    
    return res

if __name__ == '__main__':
    n = int(input())
    a = input().strip()
    b = input().strip()
    print(solve(n, a, b))