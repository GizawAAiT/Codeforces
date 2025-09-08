def solve(kth):
    num = 0
    while kth:
        num += 1
        if not (num % 3 == 0 or num%10 == 3):
            kth -= 1
    
    return num

for t in range(int(input())):
    k = int(input())
    print(solve(k))