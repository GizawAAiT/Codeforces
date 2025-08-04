from collections import Counter

def calculate_max_escapes(hole_position, mouse_positions):
    position_counts = Counter(mouse_positions)
    cat_pos = 0
    escaped = 0

    while position_counts:
        # Find mice ahead of cat
        safe_mice = [pos for pos in position_counts 
                    if pos > cat_pos]
        if not safe_mice:
            break

        # Move rightmost mouse
        move_pos = max(safe_mice)
        position_counts[move_pos] -= 1
        if position_counts[move_pos] == 0:
            del position_counts[move_pos]

        # Mouse moves right
        new_pos = move_pos + 1
        if new_pos == hole_position:
            escaped += 1
        else:
            position_counts[new_pos] += 1

        # Cat moves right and catches mice
        cat_pos += 1
        if cat_pos in position_counts:
            del position_counts[cat_pos]

    return escaped

def save_mice_opt(n, xs):
    dist = sorted((n - x for x in xs))     # ascending d_i
    cat = 0
    saved = 0
    for d in dist:
        if cat + d < n:
            saved += 1
            cat += d
        else:
            break
    return saved
def calculate_max_escapes(hole_position, mouse_positions):
    sorted_mice = sorted(mouse_positions, reverse=True)
    escaped = 0
    current_turn = 0

    for pos in sorted_mice:
        if 2 * pos - 1 >= hole_position:
            if current_turn < pos:
                escaped += 1
                current_turn += 1

    return escaped

from collections import Counter

def save_mice_bruteforce_(n: int, positions,  s = 1):
    """
    Brute simulation: O(total_steps) time,
    where total_steps ≤ (n-1)*k in the worst case.
    """
    mice = Counter(positions)           # multiset of coordinates
    cat   = 0
    saved = 0

    # Continue while at least one mouse is still on the line
    while mice:
        # --- mouse move ---
        # choose the right-most mouse still ahead of the cat
        candidate_positions = [p for p in mice if p > cat]
        if not candidate_positions:     # all remaining mice are already eaten
            break

        x = max(candidate_positions)
        mice[x] -= 1
        if mice[x] == 0:
            del mice[x]

        x += 1                          # mouse steps right by 1
        if x == n:                      # dives into the hole
            saved += 1
        else:
            mice[x] += 1

        # --- cat move ---
        cat = min(cat + s, n)
        # remove (eat) every mouse at or left of the cat
        eaten = [p for p in mice if p <= cat]
        for p in eaten:
            del mice[p]

    return saved

def save_mice_optimal_(n: int, positions, s=1):
    """
    Greedy optimal: O(k log k) time (sorting) and O(k) space.
    """
    # sort mice furthest to the hole first
    xs = sorted(positions, reverse=True)

    total_time = 0     # Σd so far
    saved      = 0

    for x in xs:
        if s * total_time < x:          # cat still left of this mouse
            saved += 1
            total_time += n - x         # add its personal walk time
        else:
            break                       # cannot start any more mice

    return saved

for t in range(int(input())):
    n, k = (int(_) for _ in input().split())
    xs = [int(_) for _ in input().split()]
    print(save_mice_optimal_(n, xs))