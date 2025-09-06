def solve(n, stones):
    removed = 0
    
    for i in range(1, n):
        if stones[i] == stones[i-1]:
            removed += 1
    
    return removed

n = int(input())
stones = input()
print(solve(n, stones))