def dormitory_room_numbers(
    n: int, m: int, a: list[int], b: list[int]) -> list[int]:
    
    idx_a, idx_b, cum = 0, 0, 0
    while idx_b < m and idx_a < n:
        
        if cum + a[idx_a] >= b[idx_b]:
            b[idx_b] = (idx_a + 1, b[idx_b] - cum)
        
            idx_b += 1
        else:
            
            cum += a[idx_a]
            idx_a += 1
    
    return b

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    
    res = dormitory_room_numbers(n, m, a, b)
    for r in res:
        print(*r)