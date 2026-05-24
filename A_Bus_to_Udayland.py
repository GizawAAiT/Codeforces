def solve(strings: list[str]) -> list[str]:
    for idx, st in enumerate(strings):
        l, r = st.split("|")
        if l == 'OO':
            strings[idx] = "++|"+r
            return strings

        if r == 'OO':
            strings[idx] = l + "|++"
            return strings
    
    return False

strings = []
for n in range(int(input())):
    strings.append(input())

sol = solve(strings)
if not sol:
    print("NO")
else:
    print('YES')
    for st in strings:
        print(st)