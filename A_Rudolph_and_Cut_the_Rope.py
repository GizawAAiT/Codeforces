def solve(nail_heignt_rope_length: list[tuple[int, int]]) -> int:
    
    num_ropes_to_be_cut = 0
    for nail_height, rope_length in nail_heignt_rope_length:
        if rope_length < nail_height:
            num_ropes_to_be_cut += 1
    
    return num_ropes_to_be_cut

for _ in range(int(input())):
    n = int(input())
    nail_heignt_rope_length = []
    for _ in range(n):
        nail_height, rope_length = map(int, input().strip().split())
        nail_heignt_rope_length.append((nail_height, rope_length))
    
    print(solve(nail_heignt_rope_length))