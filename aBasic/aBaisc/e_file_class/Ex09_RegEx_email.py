"""
    이메일 주소의 적합성 체크
        kim@encore.com   : 올바른 이메일
        kim@encore       : 잘못된 이메일 ( . 하나 없어서 )
        kim_@encore.com  : 잘못된 이메일 ( 특수문자 안됨 )

     [참고]
        ^[]: 시작
        [^] : not
        {2,9} : 최소 2개 최대 9개
        {2,} : 최소 2개만 지정하고 최대는 지정하지 않음
        $ 끝
"""
import re


# def email_check(email):
#     # 여기에 코드 작성
#     p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
#     if p.match(email) != None:
#         return '올바른 이메일'
#     else:
#         return '잘못된 이메일'
#
#
# print(email_check('kim@encore.com'))  # 올바른 이메일
# print(email_check('kim@encore'))  # 잘못된 이메일 ( . 하나 없어서 )
# print(email_check('k!m_@encore.com'))  # 잘못된 이메일 ( 특수문자 안됨 )

import re


def email_check1(email):
    # 여기에 코드 작성
    exp = re.findall('[a-z0-9A-Z]@[a-z]+\.[a-z]+$', email)
    if len(exp) == 0:
        print('잘못된 이메일')
    else:
        print('올바른 이메일')

email_check1('kim@encore.com')  # 올바른 이메일
email_check1('kim@encore') # 잘못된 이메일 ( . 하나 없어서 )
email_check1('k!m_@encore.com')  # 잘못된 이메일 ( 특수문자 안됨 )


# 정규표현 - 패스워드