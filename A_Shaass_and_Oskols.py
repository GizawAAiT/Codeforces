def solve(n: int, a: list[int], m: int, shots: list[tuple[int, int]]) -> list[int]:
    
    for x, y in shots:
        if x > 1:
            a[x-2] += y-1
        
        if x < n:
            a[x] += a[x-1] - y
        
        a[x-1] = 0
    
    return a

if __name__ == "__main__":
    n = int(input())
    a = [int(_) for _ in input().split()]
    m = int(input())
    shots = [tuple(map(int, input().split())) for _ in range(m)]
    ans = solve(n, a, m, shots)
    # Print line by line
    for num in ans:
        print(num)