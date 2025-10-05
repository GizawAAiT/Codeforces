def solve(n: int, m: int, k: int, a: list[int], b: list[int]):
    
    def num_of_complement(num, b):
        l, r = -1, len(b)
        while l<r-1:
            mid = l + (r-l)//2
            if num + b[mid] <= k:
                l = mid
            else:
                r = mid
        
        return l+1
    
    b.sort()
    
    total = 0
    for num in a:
        total += num_of_complement(num, b)
    
    print(total)
    
for t in range(int(input())):
    n, m, k = (int(_) for _ in input().split())
    a = [int(_) for _ in input().split()] 
    b = [int(_) for _ in input().split()]
    solve(n, m, k, a, b)