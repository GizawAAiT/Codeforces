def solve(inp: str, pi_ref: str = '314159265358979323846264338327'):
    iter_range = min(len(inp), len(pi_ref))
    count = 0
    for idx in range(iter_range):
        if inp[idx] == pi_ref[idx]:
            count += 1
        else: break

    print(count)

for t in range(int(input())):
    inp = input()
    solve(inp)