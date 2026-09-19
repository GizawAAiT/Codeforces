def construct_binary_string_with_k_consecutive_equal_elems(n: int, k: int
                                                           ) -> str:
    """
    - If k is n - 1, we can not construct [return -1]. Base case
    - Split k into (k)//2 and (k+1)//2. We can put ((k)//2 + 1) 0s to obtain 
    (k)//2 consecutive equal emements. Then we can put ((k+1)//2 + 1) 1s to 
    obtain ((k+1)//2) consecutive equal elements. This gives us k consecutive equal 
    elements.
    - Append or fill the rest of the string with 0 and 1 alternatively.
    """
    
    if k == n - 1:
        return -1
    
    ans =  '0' * ((k)//2 + 1) if k > 1 else ''
    ans += '1' * ((k+1)//2 + 1) if k > 0 else ''
    
    # fill the rest.  in a loop, if ans is '' or last char is 0 append 1 else append 0 until we reach n.
    for idx in range(len(ans), n):
        if ans == '' or ans[-1] == '1':
            ans += '0'
        else:
            ans += '1'
           
    return ans

if __name__ == '__main__':
    for t in range(int(input())):
        n, k = map(int, input().split())
        print(construct_binary_string_with_k_consecutive_equal_elems(n, k))