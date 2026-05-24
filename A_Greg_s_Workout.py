def solve(n: int, arr: list[int]) -> str:
    counts = [0] * 3
    for idx, repeat in enumerate(arr):
        counts[idx%3] += repeat
    
    max_idx = counts.index(max(counts))
    mapping = ["chest", "biceps", "back"]
    
    return mapping[max_idx]

n = int(input())
arr = [int(_) for _ in input().split()]
print(solve(n, arr))