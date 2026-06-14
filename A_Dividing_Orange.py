def devide_oranges(n: int, k: int, a: list[int]) -> list[int]:
    
    division = [[a[idx]] for idx in range(k)]
    
    # add safety empty list in the end:
    division.append([])
    
    # Lets change a into hashset then:
    a = set(a)
    
    idx = 0
    for num in range(1, n*k+1):
        if len(division[idx]) >= n:
            idx += 1
            
        if num not in a:
            division[idx].append(num)
        
    
    return division

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = [int(_) for _ in input().split()]
    sol = devide_oranges(n, k, a)
    for row in sol:
        print(*row)