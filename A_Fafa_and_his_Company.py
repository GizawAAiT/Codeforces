def solve(n: int):
    num_of_arrangement: int = 0
    for num_of_leads in range(1, (n+1)//2 + 1):
        if (n-num_of_leads) % num_of_leads == 0:
            num_of_arrangement += 1
    
    print(num_of_arrangement)

n = int(input())
solve(n)