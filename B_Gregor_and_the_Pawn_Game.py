def max_number_of_paws_moved(n: int, row1: list[int], row2: list[int]) -> int:
    """
    1. If direct above is 0, move the pown up, and increase counter by 1.
    2. If direct above is 1, and left diagonal is 1, move the pown to it, and 
    increase the counter by 1.
    3. If direct above is 1, and right diagonal is 1, move the pown to it, and
    increase the counter by 1, and mark the cell as 0.
    """
    cnt = 0
    for idx in range(n):
        if row2[idx] == 0: continue
        
        if row1[idx] == 0:
            cnt += 1
        elif idx > 0 and row1[idx - 1] == 1:
            cnt += 1
        elif idx < n - 1 and row1[idx + 1] == 1:
            cnt += 1
            row1[idx + 1] = 0
        
    return cnt

if __name__ == "__main__":
    for t in range(int(input())):
        n = int(input())
        row1 = [int(_) for _ in list(input())]
        row2 = [int(_) for _ in list(input())]
        print(max_number_of_paws_moved(n, row1, row2))