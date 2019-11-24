"""
        숫자형 종류
            - 정수형
            - 실수형
            - 복소수형 1 + 2j, 3i  ( 많이 사용안함 )
            - 8진수   0o25
            - 16진수  0x25
"""

# 파이션의 모든 자료형은 객체로 취급한다
# 실행 : ctrl + shift + F10
from builtins import print

""" [ 기초 연산자 ]
        + : 더하기
        - : 빼기
        * : 곱하기
        / : 나누기(실수값 결과)
        // : 나누기(정수값 결과)
        % : 나머지
        ** : 자승
    
    2. 관계연산자
        <   >   <=  >=  ==  !=
    
    3. 논리연산자
        not     or      and
        
    4. 이진(비트) 연산자
        ~   :  이진 not   
        |   :  이진 or
        &   :  이진 and
        ^   :  이진 xor
        <<  :  shift
        >>  :  shift
        
    5. 대입연산자
        =
        +=  -=  *=  /=  //= %=
        &=  |=  ^=
        >>= <<=
    
    6. 기타연산자 : 딕셔너리, 문자열, 리스트, 튜플 등의 자료형에서 사용
        is      : 비교하는 객체의 주소가 같으면 true, 다르면 false
        is not  : 비교하는 객체의 주소가 다르면 true, 같으면 false 
        in      : 요소에 포함되면 true, 없으면 false
        not in  : 요소에 포함되지 않으면 false, 없으면 true
               
"""

# a = 5
# b = 2

# print('a+b=',a+b)
# print('a-b=',a-b)
# print('a*b=',a*b)
# print('a/b=',a/b)
# print('a//b=',a//b)
# print('a%b=',a%b)
# print('a**b=',a**b)

""" [ 출력결과 ] 
        a + b = 7
        a - b = 3
        a * b = 10
        a / b = 2.5
        a // b = 2
        a % b = 1
        a ** b = 25
"""

# a++ a-- --a ++a 같은 증가/감소 연산자 없음

# print('a//b =' +str(a//b) # 문자열 + 숫자 -> 문자열 변경이 되지 않고 에러

# 출력 포맷

# y = 8.3/2.7
# print(y)
# print('실수: {0}, 점수:{1}'.format(y,100))
# print('실수: {},정수: {}'.format(y,200))
# print('실수: {1}, 정수: {0:.1f}'.format(y,300))


# 기타연산자 ( 자료의 주소를 비교 )
#
# print('hello' is 'hello') # 결과? true
# print('hello' is not 'hello') # 결과? false
# print('H' is 'Hello') # 결과 ? false
# print('H' not in 'Hello') # 결과? false

# 1

# a = 777
#
# b = 777
#
# print(a == b, a is b)

# true true
# 에디터에 따라 다름 cmd python console 에서는 true false 나옴

# 2 메모리 삭제 위한 명령어
# 2. 다음 중 변수를 메모리에서 삭제하기 위해 사용하는 명령어는?
#
# ➀ del ➁ delete ➂ remove ➃ pop ➄ clear

# del

# 3

# a = 3.5
# b = int(3.5)
# print(a**(a//b)*2)
# #>> 7.0
# print(((a - b) * a) // b)
# #>> 0.0
# b = (((a - b) * a) % b)
# print(b)
# #>> 1.75
# print((a * 4) % (b * 4))
# #>> 0.0

# 4
# celsius = float(input("섭씨온도를 입력하세요:"))
# fahrenheit = (( 9 / 5) * celsius) + 32
# print("섭씨온도:", celsius, "화씨온도:", fahrenheit)

# 정답 4

# 5 다음 변수의 자료형
# a = 'True'
# 2 번 문자형

# 6
# a = 10.6
# b = 10.5
#
# print(a * b)
# #>>111.3
# print(type(a + b))
# #>> <class 'float'>


# 7

# a = "3.5"
# b = 4
# print(a * b)
# #>>3.53.53.53.5

# 8
# a="3.5"
# b="1.5"
# print(a+b)
#
# #>> 3.51.5

# 9
# a = '3'
# b = float(a)
# print(b ** int(a))
#
# #>> 27.0

# 10
# 10. 변수(variable)에 대한 설명으로 틀린것은?
#
# ① 프로그램에서 사용하기 위한 특정한 값을 저장하는 공간이다.
#
# ② 선언되는 순간 메모리의 특정 영역에 공간이 할당된다.
#
# ③ 변수에 할당된 값은 하드디스크에 저장된다.
#
# ④ A = 8은 "A는 8이다"라는뜻이 아니다.
#
# ⑤ ‘2x + 7y’는 14라고 하면, 이 식에서 x와 y가 변수이다.
# >> 4번

# 11
# a ='20'
# b ='4'
# print(type(float(a/b)))
#
# # >> 5번

# 12

# a = "Gachon"
# b = "CS"
# c = 200
# c = int(c/4)
# print(a,b,c)

# #>> Gachon CS 50

# 13
#13.변수명을 지을 때 권장하는 규칙 중 틀린 것은?

# ① 변수명은 알파벳, 숫자, 언더스코어(_) 등을 사용하여 표현할 수 있다.
# ② 변수명은 의미 있는 단어로 쓰는 것을 권장하며, 한글도 사용할 수 있다.
# ③ 변수명은 대소문자가 구분된다.
# ④ 문법으로 사용되는 특별한 예약어는 변수명으로 쓰지 않는다.
# ⑤ 변수명은 “a”, “b” 등으로 사용하는 것은 권장하지 않는다.

# >> 2,5번