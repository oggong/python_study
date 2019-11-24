""" 1. 모듈 전체를 참조할때 import"""

# import mymodule
#
# today = mymodule.get_weather()
# print('오늘의 날씨는', today)
# print(mymodule.get_date(),'요일 입니다')


# 파일을 모듈이라고 부른다 !!!!!!!!!!!!!!


"""2. 모듈에 별칭 부여 """
# import mymodule as my
# today = my.get_weather()
# print('오늘의 날씨는', today)
# print(my.get_date(),'요일입니다')

"""3. 모듈에서 필요한 부분만 import"""
# from mymodule import get_weather,get_date
# today = get_weather()
# print('오늘의 날씨는', today)
# print(get_date(),'요일입니다') # mymodule.get_date 하여도 error
# mymodule 의 get_weather 만 가져오기 때문에 다른것도 쓰려면 추가시켜줘야 함

# 별칭 가능
# from mymodule import get_weather as gw
# today = gw()
# print('오늘의 날씨는', today)



