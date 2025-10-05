def solve(a:str):
    b = ''
    _map = {'p': 'q', 'q': 'p'}
    for chr in a[::-1]:
        if chr != 'w':
            b += _map[chr]
        else:
            b += chr
    
    print(b)
    
for t in range(int(input())):
    a = input()
    solve(a)