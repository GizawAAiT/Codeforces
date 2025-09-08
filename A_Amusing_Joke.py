from collections import defaultdict
def solve(a, b, c):
    ab = a+b
    
    cnt_ab = defaultdict(int)
    cnt_c = defaultdict(int)
    
    for chr in ab:
        cnt_ab[chr] += 1
    
    for chr in c:
        cnt_c[chr] += 1
        
    for key in cnt_ab.keys():
        if cnt_ab[key] != cnt_c[key]:
            return 'NO'
    
    for key in cnt_c.keys():
        if cnt_ab[key] != cnt_c[key]:
            return 'NO'
    
    return 'YES'

a = input().strip()
b = input().strip()
c = input().strip()

print(solve(a, b, c))