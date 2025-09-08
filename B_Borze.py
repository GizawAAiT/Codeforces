def solve(bronze):
    st = []
    res = ''
    for chr in bronze:
        if chr == '.':
            if st: 
                res += '1'
                st.pop()
            else:
                res += '0'
            
        else:
            
            if st:
                res += '2'
                st.pop()
            else:
                st.append('_')
    
    return res

bronze = input().strip()
print(solve(bronze))