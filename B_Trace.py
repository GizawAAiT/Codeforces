from math import pi

def trace_total_red_areas(n: int, r: list[int]) -> float:
    r.sort(reverse=True)
    
    r_square = 0
    for idx in range(n):
        r_square += (-1)**(idx) * r[idx] ** 2
    
    return round(pi * r_square, 4)

if __name__ == '__main__':
    n = int(input())
    r = [int(_) for _ in input().split()]
    print(trace_total_red_areas(n, r))