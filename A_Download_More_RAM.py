def solve(n: int, k: int, a: list[int], b: list[int]) -> int:
    """
    n: num of software to be run to increase RAM.
    k: initial RAM size.
    a: ai is temporary RAM needed to run the i-th software.
    b: bi is permanent RAM gained from running the i-th software.
    
    returns:
        int: final RAM size.
    """
    
    # Loop (using for) over the software and see which software can be run(based on RAM available) 
    # Out of those softwares, whats the maximum gain in RAM?
    for _ in range(n):
        max_gain, indx = 0, 0
        for i in range(n):
            if a[i] <= k and b[i] > max_gain:
                max_gain = b[i]
                indx = i                
        
        if max_gain == 0:
            break
        
        k += max_gain
        b[indx] = 0  # mark this software as used by setting its gain to 0, so that it won't be used again.
    
    return k

if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        print(solve(n, k, a, b))