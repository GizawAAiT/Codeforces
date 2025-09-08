def solve(two_digit_int):
    return two_digit_int //10 + two_digit_int%10

for t in range(int(input())):
    n = int(input())
    print(solve(n))