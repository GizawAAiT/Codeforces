def solve(k2: int, k3: int, k5: int, k6: int) -> int:
    num256 = min(k2, k5, k6)
    num32 = min(k2-num256, k3)
    
    return num256 * 256 + num32 * 32

k2, k3, k5, k6 = map(int, input().split())
print(solve(k2, k3, k5, k6))