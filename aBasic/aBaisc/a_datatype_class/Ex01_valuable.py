"""
    파이션  - 무료이지만 강력하다
        ` 만들고자 하는 대부분의 프로그램 가능
        ` 물론, 하드웨어 제어같은 복잡하고 반복 연산이 많은 프로그램은 부적절
        ` 그러나, 다른언어 프로그램을 파이썬에 포함 가능 
        
    [주의] 줄을 맞추지 않으면 실행 안됨

    [실행] Run 메뉴를 클릭하거나 단축키로 ctrl + shift + F10

    [도움말] ctrl + q

"""

""" 여러줄 주석 """
# 한줄 주석

# print("헬로우")
# print('hello')
# print("""안녕""")
# print('''올라''')


# 실행 : ctrl + shift + F10

# 작은 따옴표 와 큰 따옴표 구별 X



'''
변수란
    파이션의 모든 자료형은 객체로 취급한다
    a = 7
            7을 가리키는 변수 a이다. ( 저장한다는 표현 안함 )
            변수 a는 7이라는 정수형 객체를 가리키는 레퍼런스이다.
            여기서 7은 기존 프로그램언어에 말하는 상수가 아닌 하나의 객체이다.
    
    [변수명 규칙]
    - 영문자 + 숫자 + _ 조합
    - 첫글자에 숫자는 안됨
    - 대소문자 구별
    - 길이 제한 없음
    - 예약어 사용 안됨       
'''

# 예약어 확인 방법

# import keyword
# print(keyword.kwlist)

'''
a = 7 # 7 객체를 가리키는 변수 a
b = 7 # 7 객체를 가리키는 변수 b

# print(type(a))
# print(a is 7) # true
# print(b is 7) # true
# print(a is b) # true

print(id(a)) # 140736113386064
print(id(b)) # 140736113386064
print(id(7)) # 140736113386064
'''

# # 여러 변수 선언
# a, b = 5, 10
# print('a+b=',a+b)
#
# # 파이썬에서 두 변수의 값 바꾸기 (swapping)
# print('A=',a,'B=',b)
# a, b = b, a
#
# print('A=',a,'B=',b)
#
# # 변수의 삭제
# del b
#
# print(b)




