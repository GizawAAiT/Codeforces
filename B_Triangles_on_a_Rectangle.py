def solve(w, h, B, T, L, R):
    INF = 10**30
    best = INF

    # Horizontal sides
    for i in range(len(B)):
        xi = B[i]
        for j in range(i + 1, len(B)):
            base = B[j] - xi
            area2 = base * h
            if area2 < best:
                best = area2

    for i in range(len(T)):
        xi = T[i]
        for j in range(i + 1, len(T)):
            base = T[j] - xi
            area2 = base * h
            if area2 < best:
                best = area2

    # Vertical sides
    for i in range(len(L)):
        yi = L[i]
        for j in range(i + 1, len(L)):
            base = L[j] - yi
            area2 = base * w
            if area2 < best:
                best = area2

    for i in range(len(R)):
        yi = R[i]
        for j in range(i + 1, len(R)):
            base = R[j] - yi
            area2 = base * w
            if area2 < best:
                best = area2

    return best

for t in range(int(input())):
    w, h = (int(_) for _ in input().split())
    
    B = [int(_) for _ in input().split()]
    T = [int(_) for _ in input().split()]
    L = [int(_) for _ in input().split()]
    R = [int(_) for _ in input().split()]
    
    print(solve(
        w, h, B[1:], T[1:], L[1:], R[1:]))