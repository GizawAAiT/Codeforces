def solve(number):
    evens = [str(i) for i in range(2, 9, 2)]
    
    if number[-1] in evens:
        return 0
    
    if number[0] in evens:
        return 1
    
    return 2 if any(d in evens for d in number) else -1

for t in range(int(input())):
    number = input().strip()
    print(solve(number))