def solve(n, k, scores):
    ptr = k-1
    while ptr < n-1 and scores[ptr+1] == scores[ptr]:
        ptr += 1
        
    while ptr >= 0 and scores[ptr] <= 0:
        ptr -= 1
    
    return ptr + 1

n, k = (int(_) for _ in input().split())
scores = [int(_) for _ in input().split()]

# Invoke the solution
print(solve(n, k, scores))