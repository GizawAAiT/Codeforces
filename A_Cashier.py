def maximum_number_of_breaks(
    n: int, L: int, a: int, tl: list[tuple[int, int]]) -> int:
    
    if n < 1:
        return L // a

    breaks = 0
    for idx in range(1, n):
        t1, l1 = tl[idx-1]
        t2, l2 = tl[idx]
        breaks += (t2 - t1 - l1) // a
    
    tn, ln = tl[-1]
    breaks += (L - tn - ln) // a
    
    t1, l1 = tl[0]
    breaks += t1 // a
    
    return breaks

if __name__ == '__main__':
    n, L, a = map(int, input().split())
    tl = []
    for _ in range(n):
        t, l = map(int, input().split())
        tl.append((t, l))
    
    print(maximum_number_of_breaks(n, L, a, tl))