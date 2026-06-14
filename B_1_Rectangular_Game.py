from math import isqrt

def largest_devisor(n: int) -> int:
    for idx in range(2, isqrt(n) + 1):
        if n % idx == 0: return n//idx
    
    return 1

def maximum_rectangular_sum(n: int) -> int:
    res = n
    while n > 1:
        largest_dev = largest_devisor(n)
        res += largest_dev
        n = largest_dev
    
    return res

if __name__ == '__main__':
    n = int(input())
    print(maximum_rectangular_sum(n))