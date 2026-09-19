def longest_erasure_time(s: str) -> int:
    
    """
    We're given a string s consisting of (#, *), # represent one cm length of 
    line or part of longer line, * represent empty space. So, s can contain 
    one or more lines init. We're required to find the longest line devided 
    by 2 (ceil devision).
    
    Approach:
     - In a single traversal, catch the longest line length.
     - return ceil(longest_line_length / 2)
    """
    
    longest_line_length = 0
    current_line_length = 0
    
    for c in s:
        if c == '#':
            current_line_length += 1
        else:
            longest_line_length = max(longest_line_length, current_line_length)
            current_line_length = 0
            
    longest_line_length = max(longest_line_length, current_line_length)
    
    return (longest_line_length + 1) // 2

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        s = input()
        print(longest_erasure_time(s))