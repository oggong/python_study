# (0) 문자열을 "" 이나 '' 으로 표현


# -----------------------------------------
# (1) 개행을 포함한 문자열
# msg = """
#     안녕하세요.
#     저는 성이 파이이고,
#     이름은 썬입니다.
#     잘 부탁합니다.
#       """
# print(msg)
#
# msg = '''
#     행복합시다
#     즐깁시다
#     오늘도
# '''
# print(msg)

# -----------------------------------------
#  (2) 문자열 연산
#       문자열 합치기 : 문자열 + 문자열
#       문자열 반복 : 문자열 * 숫자

# a = '독도는 '
# b = "한국이다. "
#
# print("-"*50)
# print(a+b)
# print("ox"*25)
# print((a+b)*3)
# print("-"*50)

# """ [ 출력결과 ]
#         --------------------------------------------------
#         독도는 한국이다.
#         oxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox
#         독도는 한국이다. 독도는 한국이다. 독도는 한국이다.
#         ==================================================
# """


# -----------------------------------------
#  (3) 문자열의 인덱싱과 슬라이싱
#       - 인덱스는 0부터 시작한다
#       - s[i] : s 문자열에서 i번째 문자 추출
#       - s[i:j] : s 문자열에서 i번째에서 j번째 전까지의 문자 추출
#       - s[i:j:k] : s 문자열에서 i번째에서 j번째 전까지에서 k개씩 건너뛰어 문자 추출
#
#       - s[-i] : s 문자열에서 뒤에서부터 i번째 문자 추출
#                 ( 뒤에서 인덱스는 1부터 센다 )

# msg ='오늘도 행복도 하다'
#
# print(msg[0])
# print(msg[0:2])
# print(msg[1:6])
# print(msg[0:6:2])
# print(msg[-1])
#
# """ [ 출력결과 ]
#         오
#         오늘
#         늘도 행복
#         오도행
#         다
# """

# """ [ 참고 ]
#        ` msg[0] == msg[-0] 같은 값을 추출
#        ` msg[:] 전체 추출
#        ` msg[i:-j] i번째부터 뒤에서 j번째 전까지 추출
# """

# msg = '오늘도 행복도 하다'
# print()
# print(msg[-0])  # 예측? 오 # 결과? 오
# print(msg[:])  # 예측? 오늘도 행복도 하다 # 결과? 오늘도 행복도 하다
# print(msg[5:-1]) # 예측?복도 하 # 결과? 복도 하
# print()

# ctrl + q 사용해서 모르는 함수 찾아보기


""" [ 확인 ]
    1- 문자열 끝까지라면 두번째 숫자 생략 가능
    2- 처음부터 시작하는 것이라면 첫번째 숫자 생략 가능
"""

# msg = '오늘도 행복도 하다'
#
# # 1) 5번째부터
# print(msg[5:])
# # 2) 5번째 전의 문자까지
# print(msg[:5])
# # 3) 5번째 전의 문자까지에서 2개씩 건너뛰어
# print(msg[:5:2])
# # 4) 문자열 전체에서 2개씩 건너뛰어
# print(msg[::2])

""" [ 연습-1 ]
    날짜와 시간을 표현하는 문자열에서 '2020-02-22 : 12:05:12'
    '2020년 2월 22일' 출력
    '12시 5분' 출력
"""
# from datetime import datetime
#
# now = datetime.now()
#
# print(now)
#
# abcd = "2020-02-22 : 12:05:12"
# print(abcd[0:4], "년", abcd[5:7], "월", abcd[8:10], "일");
# print(abcd[-8:-6],"시",abcd[-5:-3],"분")

# -----------------------------------------
#  (4-1) 문자열 관련 함수
#       s.count('글') : s 문자열에서 '글'이라는 문자 개수 세기
#       s.index('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.find('글') : s 문자열에서 문자 '글' 위치 알려주기
#       s.rfind('글') : s 문자열에서 문자 '글' 오른쪽에서 왼쪽으로 찾아서 위치 알려주기
#       s.len() : s 문자열 길이

""" [ 연습문제 ]
    1) '행복'이라는 글자 위치 찾기
    2) '가자'라는 글자 위치 찾기
    3) '행복'이라는 글자를 오른쪽에서 왼쪽으로 찾기
    4) 문자열 전체 길이 구하기
    5) '도'라는 단어의 갯수 구하기
"""
# msg = '오늘도 행복도 하다'
#
# print(msg.index('행복'))  # 4
# print("행복", msg.find("행복"))  # 4
# # print(msg.index('가자')) # error
# print("가자", msg.find("가자"))  # -1
# print("찾기", msg.rfind("행복"))  # 4
# print("문자열 전체 길이", len(msg)) # 10
# print("도 갯수", msg.count("도"))  # 2
# print()

""" [ 출력결과 ]
    1) 4
    2) -1
    3) 4
    4) 10
    5) 2
"""
# -----------------------------------------
#  (4-2) 문자열 관련 함수
#   s.upper() : 소문자를 대문자로
#   s.lower() : 대문자를 소문자로
#   s.lstrip() : 왼쪽 공백 지우기
#   s.rstrip() : 오른쪽 공백 지우기
#   s.strip() : 양쪽 공백 지우기

msg = '  This is My Life  '
#
# print("소문자를 대문자로",msg.upper())
# print("대문자를 소문자로",msg.lower())
# print("왼쪽 공백 지우기",msg.lstrip())
# print("오른쪽 공백 지우기",msg.rstrip())
# print("양쪽 공백 지우기",msg.strip())

# 모든 공백 지우기
# print("모든 공백 지우기",msg.replace(" ",""))


# -----------------------------------------
#  (4-3) 문자열 관련 함수
#   s.replace("a","b")  :  s 문자열에서 단어 a를 단어 b로 바꾸기
#   s.split() : s 문자열을 공백으로 나누기
#   s.split('z') : s 문자열을 z 기호로 나누기
#   d.join(s) : d 단어를 s 문자열에 삽입

# msg = "우리는 독도를 지킨다"
# print(msg)
# print("독도 -> 대한민국 바꾸기 >>",msg.replace("독도","대한민국"))
# # replace 함수는 원본을 변경하지 않고 새로운 객체를 만듬
#
# print("문자를 삽입 >> ",','.join(msg)) # msg.join(',') 이 아님

# -----------------------------------------
#  (5) 문자열 포맷
    # (1) format() 이용
    # (2) % 이용
    # %이용이 format() 보다 속도가 빠르지만 코드 깔끔하게 작성하는 것이 중요하다


# msg = '{}님 오늘도 행복하세요'
# print(msg.format('홍길동'))

# msg = '{}님 오늘도 행복하세요- {}으로부터'
# # 순서대로 입력
# print(msg.format('홍길동','대한민국'))
#
# msg = '{name}님 오늘도 행복하세요- {group}으로부터'
# print(msg.format(group='대한민국',name='홍길동'))

# name = '홍길자'
# age = 25
# height = 160.9
#
# print('%s님은 %d살이고, 키는 %.2f cm 입니다' % (name,age,height))

# msg = '{0}님 오늘도 행복하세요- {1}으로부터'
msg = '{1}님 오늘도 행복하세요- {0}으로부터'


msg = '{name}님 오늘도 행복하세요- {group}으로부터'

# [참고] http://pyformat.info


# 자바쌤 카페 문제

#1. 다음 코드의 실행 결과로 알맞은 것은?

# a = 11
# b = 9
#
# print('a'+'b')

# 답 3 ab

#2. 다음 코드의 실행 결과로 알맞은 것은?

# fact = "Python is funny"
# print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))

# 답 2 21

# 3. 다음 코드의 실행 결과로 알맞은 것은?

# text = 'Gachon CS50 - programming with python'
#
# text2 = " Human cs50 knowledge belongs to the world "
#
# text.lower()
#
# print(text[:5] + text[-1] + text[6] + text2.split()[0])

# 답 1

# 4. 다음 코드의 실행 결과로 알맞은 것은?
# class_name = 'introduction programming with python'
#
# for i in class_name:
#
# if i == 'python':
#
# i = i.upper()
#
# print(class_name)

# 답 1

# 5. 다음 코드의 실행 결과를 쓰시오.

# a = '10'
# b = '5-2'.split('-')[1]
# print(a*3+b)

# 답 1010102

# 6. 다음 코드의 실행 결과를 쓰시오.


# a = "abcd e f g"
#
# b = a.split()
#
# c = (a[:3][0])
#
# d = (b[:3][0][0])
#
# print(c + d)

# 답 aa

# 7. 다음 코드의 실행 결과를 쓰시오.

# result = "CODE2018"
#
# print("{0},{1}".format(result[-1], result[-2]))

# 답 8,1

'''
8. 다음 중 문자열 함수의 설명으로 틀린 것은?

① capitalize( ): 첫 문자를 대문자로변환한다.

② title( ): 각 단어의 앞 글자만대문자로 변환한다.

③ strip( ): 공백을 기준으로 나눠리스트를 반환한다.

④ isdigit( ): 문자열이 숫자인지의여부를 반환한다.

⑤ upper( ): 문자를 대문자로 변환한다.
'''

# 답 3

# msg = 'this is greatest show '
#
# print(msg.capitalize())
# print(msg.title())
# print(msg.strip())
# print(msg.isdigit())
# print(msg.upper())

