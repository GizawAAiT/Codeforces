def solve(expression):
    a, b = (int(_) for _ in expression.split('+'))
    
    return a+b

for t in range(int(input())):
    expression = input()
    print(solve(expression))    