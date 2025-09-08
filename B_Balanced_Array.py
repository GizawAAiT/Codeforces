def solve(n):
    ans = []
    
    # first half
    for ev in range(n//2):
       ans.append(ev*2+2) 
    
    # second half:
    for od in range(n//2):
        ans.append(od*2+1)
    
    # last:
    ans[-1] += (n//2)
    
    return ans

if __name__== "__main__":
    for t in range(int(input())):
        n = int(input())
        
        if n%4:
            print('NO')
        
        else:
            print('YES')
            print(*solve(n))