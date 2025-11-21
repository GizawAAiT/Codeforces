def solve(qaq: str) -> int:
    n, count = len(qaq), 0
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if qaq[i] == 'Q' and qaq[j] == 'A' and qaq[k] == 'Q':
                    count += 1
    return count

qaq = input().strip()
print(solve(qaq))