def f(n):
    if n%2: # Odd case
        return (-1-n)//2
    
    return 2*n //4 #Even case      
    
print(f(int(input())))