def max_happy_quadratic(times: list[int]) -> int:
    """Correct but slow O(n²) solution."""
    queue = []                     # accepted (happy) customers
    for t in sorted(times):        # ascending order
        if sum(queue) <= t:        # recompute prefix each time  ← O(len(queue))
            queue.append(t)        # keep him happy
        # else: skip (place later, will be unhappy)
    return len(queue)

n = int(input())
print(max_happy_quadratic(times=[int(_) for _ in input().split()]))