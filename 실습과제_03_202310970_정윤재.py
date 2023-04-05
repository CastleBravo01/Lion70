num = str(input("주민등록번호:")) #000000-0000000
year = int(num[0:2]) 
month = int(num[2:4])
date = int(num[4:6])
tf = 0
if len(num) == 14 and num[6] == "-": #전체 글자 수 체크 및 '-'유무
    pass
else: tf = 1
if month == 2:
    if (year%4) == 0 and date <= 29: #윤년 판별
        pass
    elif (year%4) != 0 and date <= 28:
        pass
    else: tf = 1
else: 
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if date > 0 and date <= 30:
            pass
        else:
            tf = 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if date > 0 and date <= 30:
            pass
        else:
            tf = 1
    else: tf = 1
if year >= 0 and year <= 23: #2000년대 출생자
    if int(num[7]) == 3 or int(num[7]) == 4:
        pass
    else:
        tf = 1
elif year >= 24 and year <= 99: #1900년대 출생자
    if int(num[7]) == 1 or int(num[7]) == 2:
        pass
    else:
        tf = 1
if tf == 0: 
    print(f"유효한 주민등록번호:{num}")
else:
    print("잘못된 주민등록번호")