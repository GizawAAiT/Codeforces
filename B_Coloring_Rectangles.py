def min_number_of_blue_cell_to_color_the_rectangle(n: int, m: int) -> int:
    option_1 = n*(m//3) + (m%3)*(n+2)//3
    option_2 = m*(n//3) + (n%3)*(m+2)//3
    return min(option_1, option_2)

if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        print(min_number_of_blue_cell_to_color_the_rectangle(n, m))