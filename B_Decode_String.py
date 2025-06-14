def solve(byt):
    base, res = ord('a')-1, []
    idx = len(byt)-1
    while idx>=0:
        if byt[idx] == '0':
            res.append(chr(base + int(byt[idx-2: idx])))
            idx -= 3  

        else:
            res.append(chr(base + int(byt[idx: idx+1])))
            idx -= 1

    res.reverse()
    return ''.join(res)

for _ in range(int(input())):
    n = input()
    byt = input().strip()
    print(solve(byt))


