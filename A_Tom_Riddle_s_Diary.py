def string_presented_in_the_stream(stream: list[str]) -> list[str]:
    result = []
    set_of_strings = set()
    for s in stream:
        if s in set_of_strings:
            result.append('YES')
        else:
            result.append('NO')
            set_of_strings.add(s)
    
    return result

if __name__ == '__main__':
    n = int(input())
    stream = [input() for _ in range(n)]
    print('\n'.join(string_presented_in_the_stream(stream)))