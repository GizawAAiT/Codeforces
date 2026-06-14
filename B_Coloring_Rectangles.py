def min_number_of_blue_cell_to_color_the_rectangle(n: int, m: int) -> int:
    return min((n+2)//3 * m, (m+2)//3 * n)

if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        print(min_number_of_blue_cell_to_color_the_rectangle(n, m))