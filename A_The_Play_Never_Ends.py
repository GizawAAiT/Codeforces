def is_spectator_on_kth_match(k: int) -> str:
    return 'YES' if (k-1)%3 == 0 else 'NO'

if __name__ == '__main__':
    for t in range(int(input())):
        k = int(input())
        print(is_spectator_on_kth_match(k))