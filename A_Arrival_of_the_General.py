def solve(n, soldiers):
    _min = _max = soldiers[0]
    for soldier in soldiers:
        _min = min(_min, soldier)
        _max = max(_max, soldier)
        
    left, right = 0, n-1
    while soldiers[left] != _max:
        left += 1
    
    while soldiers[right] != _min:
        right -= 1
    
    total = left + (n-right-1)
    return total if left < right else total -1

n = int(input())
soldiers = [int(_) for _ in input().split()]
print(solve(n, soldiers))