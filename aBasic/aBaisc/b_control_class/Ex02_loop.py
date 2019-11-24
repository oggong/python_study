
# ------------------------------------------------------
"""
   (2) for문
        for <타켓변수> in 집합객체 :
            문장들
        else:
            문장들

        ` 반복문 뒤에 else는 반복하는 조건에 만족하지않으면 실행 ( 많이 사용 안함 )

   (3) while 문
        while 조건문 :
            문장들

"""

a = 112                  # 숫자형
b = ['1','2','3']       # 리스트
c = '987'                # 문자열
d = tuple(b)             # 튜플
e = dict(k=5, j=6)       # 딕셔너리

# for entry in a: # a는 반복이 안되지만 b부터 e까지는 반복된다.
#    print(entry)

# for entry in d: # a는 반복이 안되지만 b부터 e까지는 반복된다.
#    print(entry)

# a error b 1,2,3 c 9,8,7 d 1,2,3 e k,j

#
# for entry in e.items():
#     print(entry)

# result : ('k', 5)
#          ('j', 6)

# 1 ~ 10 까지의 합

# sum = 0
# for i in range(1,11):
#     sum += i
#     print(sum, end=" ")

# 1 ~ 10 까지의 합 // 홀수의 합

# sum = 0
# for i in range(1,11,2):
#     sum += i
# print(sum, end=" ")

# 2단 부터 9단까지 구구단 출력

# 출력 형식
# print("#"*50)
# for x in range(2,10):
#     for y in range(1,10):
#         print("{0} * {1} = {2}".format(x,y,x*y))
#     print()
#     print("#"*50)

# =========================================================
# while

# a = 1
# while True:  # 무한루프
#    if a == 1:
#        print(a)
#        break

# a = ['z','y','x']
# while a:
#     print(a.pop())
# else:
#     print('end')

# x y z end

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~

a = ['z','y','x']
while a:
    data = a.pop()
    if data == 'y':
        break
else:
    print('end')











"""
[과제] 2단부터 9단까지 이중 반복문으로 출력
"""
