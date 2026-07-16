def min_number_of_second_required(n: int, c: int, a: list[int], b:
    list[int]) -> int:
    
    reordered = 0
    for idx in range(n):
        if a[idx] < b[idx]:
            a.sort()
            b.sort()
            reordered = c
            break
    
    for idx in range(n):
        if a[idx] < b[idx]:
            return -1
    
    return sum(a) - sum(b) + reordered

for t in range(int(input())):
    n, c = map(int, input().split())
    a = [int(_) for _ in input().split()]
    b = [int(_) for _ in input().split()]
    print(min_number_of_second_required(n, c, a, b))