def min_turns_optimal(a):
    n = len(a)
    hacked = [False]*n
    have = 0
    pos, dir_ = 0, 1          # start at computer 1, moving right
    turns = 0

    while have < n:
        # hack current computer if possible
        if not hacked[pos] and have >= a[pos]:
            hacked[pos] = True
            have += 1
            continue          # stay and check again (maybe multiple hacks)

        nxt = pos + dir_
        # need to reverse at array end
        if nxt < 0 or nxt >= n:
            dir_ *= -1
            turns += 1
        else:
            pos = nxt         # just walk

    return turns


n = int(input())
a = [int(_) for _ in input().split()]
print(min_turns_optimal(a))