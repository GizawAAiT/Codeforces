def solve(n: int, t: int, queue: list[str]):
    for _ in range(t):
        idx = 1
        while idx < n:
            if queue[idx-1] == 'B' and queue[idx] == 'G':
                queue[idx-1], queue[idx] = 'G', 'B'
                idx += 2
            else: idx += 1
        
    return ''.join(queue)

n, t = (int(_) for _ in input().split())
queue = list(input().strip())
print(solve(n, t, queue))