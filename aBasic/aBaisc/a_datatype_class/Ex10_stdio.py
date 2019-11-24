"""
    [ 콘솔 입력 처리 함수 ]
    - input() : 기본적으로 문자열로 입력받음
    - eval() : 함수로 감싸면 숫자 처리됨

"""
# name = input('이름은?')
# print('당신은 {0}입니다'.format(name))
# # print('당신은 %s 입니다' % name)
#
# # 나이를 입력받아서 한 살을 더해서 출력
# age = int(input('나이는?'))
# print('당신은 {0}세 입니다'.format(age+1))

# print('1+2') # 예측 -> 결과 확인
# print(eval('1+2'))


# ----------------------------------
# 단을 입력받아 구구단을 구하기
# x = int(input('단을 입력하세요 >>'))
# for y in range(1,10):
#     print(x*y)

# -----------------------------------------
# print() 함수
print('안녕', '친구')  # 한칸 띄어쓰기
print('안녕' + '친구')  # 붙여 쓰기
print('안녕', '친구')  # 한칸 띄어쓰기

for i in range(5):
    print(i, end=' ')  # 개행 없애기

# -------------------------------------------------------
# 명령행 매개변수 받기 - java의 main() 함수의 인자
# [ 콘솔에서 실행 ] python Ex10_stdio.py ourserver scott tiger
#                                   0         1      2      3
import sys

args = sys.argv[2:]  # scott tiger 만 얻어오기
for i in args:
    print('정보 :', i)
