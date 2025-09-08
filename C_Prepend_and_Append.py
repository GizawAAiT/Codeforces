def solve(n, binary):
    l, r = 0, n-1
    while l<r and binary[l] != binary[r]:
        l+= 1
        r-= 1
    
    return r-l+1

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        binary = input().strip()
        
        print(solve(n, binary))