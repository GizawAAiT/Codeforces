def solve(string: list[chr]):
    for idx in range(1, len(string)):
        if string[idx] != string[idx-1]:
            string[idx], string[idx-1] = string[idx-1], string[idx]
            return ''.join(string)
    
    return False

for t in range(int(input())):
    string = list(input())
    res = solve(string)
    
    if not res:
        print('NO')
    
    else:
        print('YES')
        print(res)