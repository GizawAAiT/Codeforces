def permutation_with_minimum_cost(n: int, k: int) -> list[int]:
    perm = []
    for idx in range(n//2):
        perm.extend([n-idx, idx+1])
    
    if n%2: perm.append((n+1)//2)
    
    return perm

if __name__ == '__main__':
    for t in range(int(input())):
        n, k = map(int, input().split())
        print(*permutation_with_minimum_cost(n, k))