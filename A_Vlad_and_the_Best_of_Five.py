def solve(string):
    count_a = count_b = 0
    for s in string:
        count_a += s == 'A'
        count_b += s == 'B'
    
    if count_a > count_b:
        return 'A'
    
    return 'B'

for t in range(int(input())):
    string = input()
    print(solve(string))