def solve(number):
    if len(number) < 3:
        return 'NO'
    
    first, second = number[:2], number[2:]
    
    if first != '10' or second[0] == '0' or int(second) < 2:
        return 'NO'
    
    return 'YES'

for t in range(int(input())):
    number = input()
    print(solve(number))