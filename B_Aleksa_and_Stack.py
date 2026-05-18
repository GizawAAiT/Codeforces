def solve(n: int) -> list[int]:
    
    ans = [1,3]
    curr = 4
    n -= 2
    while n>0:
        if 3*curr % (ans[-1] + ans[-2]) != 0:
            ans.append(curr)
            n -= 1
            
        curr += 1
    
    return ans

for _ in range(int(input())):
    n = int(input())
    print(*solve(n))