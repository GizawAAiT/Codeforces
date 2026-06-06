def maximum_total_number_of_slices_Hao_can_eat(n: int) -> int:
    return (n-1)//2

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        print(maximum_total_number_of_slices_Hao_can_eat(n))