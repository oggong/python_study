"""
import datetime
today = datetime.date.today();
print('today is ', today)
"""

from datetime import date
today = date.today();
print('today is ', today)

print(today.year)
print(today.month)
print(today.day)

# 현재의 날자와 시간 구하기 연월일 시분초 다나옴
from datetime import datetime
current_time = datetime.today()
print(current_time)

# 날짜 계산
from datetime import timedelta
today = date.today()
print('어제',  today+timedelta(days=-1))

# 날짜 출력 형식 (strftime() 이용)
today = datetime.today()
print(today)
print(today.strftime('%Y-%m-%d'))
print(today.strftime('%d/%m/%Y %H:%M'))

# 문자열로 날짜형식으로 변환(strfptime() 이용)
str = '2020-08-20 12:25:33'
mydate = datetime.strptime(str,'%Y-%m-%d %H:%M:%S')
print(mydate)
print(type(mydate))