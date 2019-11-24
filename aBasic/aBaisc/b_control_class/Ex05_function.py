"""
    [ 함수 ]

     반복적인 구문을 만들어 함수로 선언하여 간단하게 호출만 하고자 한다

     def 함수명(매개변수):
        수행할 문장들
"""
#(0) 인자도 리턴값도 없는 함수

# def func():
#     print('func inside')
# func()
# print(func()) # 리턴 값이 없으면 None 반환

# (1) 인자도 리턴값도 있는 함수 : 리턴값이 여러개 가능

def func(arg1,arg2):
    return arg1*2 , arg2+10
# print(func(2,3))


# 함수 호출 후 리턴값을 변수에 지정해서 출력

# a,b = func(2,3)
# print(a,b) # a 와 b 각각 하나씩 넣기
#
# a = func(2,3)
# print(a) # 튜플로 하나에 받기

#(2) 위치 인자 positional argument

# def func(greeting,name):
#     print(name,'님','!!!!',greeting)
# func('안녕하세요','홍길자')
# func('홍길동','하이')

# (3) 키워드 인자 (keyword argument)

# func(name='길동아',greeting='몰라')

# (4) 기본 매개변수 지정

# func("안녕") # error 한개만 지정 햇을때
# def func(greeting , name='홍길동'):
#     print(name,'님','####',greeting)
# func("안녕","홍길숙")
# func("안녕")

# def buggy( arg, result=[]):
#     result.append(arg)
#     print(result)
# buggy('ㅁ')
# buggy('R')
# buggy('A',[1,2,3,4]) # [1,2,3,4,'A']
# buggy('z')



'''
1번째와 2번째는 인자가 반드시 들어가고 3번째는 인자가 들어갈 수도 있고 없으면 0으로 초기화한다
그러나 4번째 인자부터는 정확히 모른다면?
print(func(4, 5))
print(func(4, 5, 6))
print(func(4, 5, 6, 7))
print(func(4, 5, 6, 7, 8, 9))       # i9에 7,8,9가 튜플로 들어간다
'''

# 위치 인자 모으기

# def func(i,j,k=0,*args): # 세번째는 안들어올걸 대비해서 0을 넣어놓기 *args : 위치 인자들
#     sum = i+j+k
#     for i in args:
#         sum += i
#     return sum
#
# print(func(4, 5))
# print(func(4, 5, 6))
# print(func(4, 5, 6, 7))
# print(func(4, 5, 6, 7, 8, 9))       # i9에 7,8,9가 튜플로 들어간다

# (6) 키워드 인자 모으기
def func(i,j,k=100,*args,**kwargs): # **kwargs : 키워드인자가 여려개인 경우
    print(i,j,k)
    print(args)
    print(kwargs)
func(1,2,3)
func(1,2,3,4,5,6)

func(1,2,3,a=100,b=200,c=300)
func(1,2,3,4,a=100,b=200,c=300)

