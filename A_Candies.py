def possilbe_x_to_breakdown_n_to_k_factors(n: int) -> int:
    k = 2
    while n % (2**k - 1) != 0:
        k += 1
    
    return n // (2**k - 1)

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        print(possilbe_x_to_breakdown_n_to_k_factors(n))