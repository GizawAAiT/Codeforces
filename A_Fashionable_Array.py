def solve(n: int, a: list[int]) -> int:
    a.sort()
    
    l_parity, r_parity = a[0]%2, a[-1]%2
    if l_parity == r_parity: return 0
    
    l_idx = 0
    while l_idx < n and a[l_idx] % 2 == l_parity:
        l_idx += 1
    
    r_idx = n-1
    while r_idx > 0 and a[r_idx] % 2 == r_parity:
        r_idx -= 1
    
    return min(l_idx, n-1-r_idx)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(_) for _ in input().split()]
        print(solve(n, a=a))