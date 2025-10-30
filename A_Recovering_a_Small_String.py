def solve(n: int):
    answer = ''
    
    third = min(n-2, 26)
    answer += chr(ord('a') + third-1)
    n -= third
    
    second = min(n-1, 26)
    answer = chr(ord('a') + second-1) + answer
    
    n -= second
    
    answer = chr(ord('a') + n-1) + answer
    
    return answer

for t in range(int(input())):
    n = int(input())
    
    print(solve(n))