def solve(seq, patterns):
    idx = 0
    for pattern in patterns:
        if pattern == seq[idx]:
            idx += 1
        
    print(idx+1)

seq = input()
patterns = input()
solve(seq, patterns)