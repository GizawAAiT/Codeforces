def solve(n, binary):
    # l = 0
    # res = 0
    
    # for r in range(n):
        
    #     while l<r and binary[l] == '1':
    #         l += 1
        
    #     if binary[r] == '0':
    #         res = max(res, r-l+1)
        
    #     else:
    #         l = r

    # return res
    
    cnt = _max_cnt = 0

    for bin in binary:
        if bin == '0':
            cnt += 1
            _max_cnt = max(_max_cnt, cnt)
        
        else: cnt = 0
    
    return _max_cnt

for t in range(int(input())):
    n = int(input())
    binary = input().split()
    print(solve(n, binary))