"""
 [ 제어문 ]
    - 파이썬은 들여쓰기를 하여 블록을 표현한다
    - 들여쓰기는 탭과 공백을 섞어 쓰지 말자

    [ex]
    if a>b:
        print(a)
            print(b)  => 에러발생

    (1) if 문
        if 조건식A :
            문장들
        elif 조건식B :
            문장들
        else :
            문장들

        ` 조건식이나 else 뒤에는 콜론(:) 표시
        ` 조건식을 ( ) 괄호 필요없다
        ` 실행할 코드가 없으면 pass
        ` 파이썬은 switch 문 없음
"""

# 거짓(False)의 값
i = 0;
i2=0.0
i3=""
i4=str()
i5=list()
i6=tuple()
i7=set()
i8=dict()
i9={}
i10=None

# (1) 간단한 if 확인
a = -1
if a:
    print('True-1') # *
else:
    print('False-1')

if not a :
    print('True-2') # 안됨


# (2) 논리 연산자 이용한 조건
a = 10
# b = -1 # 둘다 True-3 True-4
b = 0 # 답이 없음
if a and b :
    print('True-3')
if a and b :
    print('True-4')

print(a and b) # b
print(a or b) # a

# (3) find() - 해당글자를 찾으면 그 글자의 인덱스 반환
#               해당 글자를 못 찾으면 -1 리턴
word = 'korea'
if word.find('k'):
    print('1>')
if word.find('z'):
    print('2>')

# 해당하는 문자가 있는 경우만 조건문 안에서 실행 (3 > 출력)

# (3) 변수
a, b = 0,1
if a:
    c = 2
elif b:
    c = 4
else:
    c = 8

print('C =', c) # 1) 2 출력 2) 4 출력 *** 3) 8 출력 4)에러





