def can_obtain_y_from_x_by_division(x: int, y: int) -> str:
    
    return "YES" if x % y == 0 else "NO"

if __name__ == "__main__":
    for t in range(int(input())):
        x, y = map(int, input().split())
        print(can_obtain_y_from_x_by_division(x, y))