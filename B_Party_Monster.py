def validate_brackets(input_str: str) -> str:
    '''
    The input string is just made up of the characters '(' and ')'.
    It's allowed to shuffle the characters in anyways to make a valid bracket
    sequence. So, simply counting the number of '(' and ')' and comparing them 
    will be enough to determine if a valid bracket sequence can be formed.
    
    Returns:
        'YES' if a valid bracket sequence can be formed, 'NO' otherwise.
    '''
    
    left_bracket_count = input_str.count('(')
    right_bracket_count = input_str.count(')')
    for c in input_str:
        if c == '(':
            left_bracket_count += 1
        else:
            right_bracket_count += 1
    
    return 'YES' if left_bracket_count == right_bracket_count else 'NO'

if __name__ == "__main__":
    for t in range(int(input())):
        n  = int(input()) # fcking useless input, but whatever
        input_str = input()
        print(validate_brackets(input_str))