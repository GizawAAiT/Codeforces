def solve(time: str):
    
    hh, mm = time.split(':')
    time_zone = 'AM' if hh < '12' else 'PM'
    
    if hh == '00': hh = '12'
    if hh > '12': hh = str(int(hh)-12)
    if len(hh) < 2: hh = '0'+hh
    return [hh + ':' + mm, time_zone]

for t in range(int(input())):
    time = input()  
    print(*solve(time))
    