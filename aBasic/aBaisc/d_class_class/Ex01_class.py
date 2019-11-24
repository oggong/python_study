"""
     1) 클래스 기초

     ` __init__ 함수 : 객체 초기화 함수( 생성자 역할 )
     ` self : 객체 자신을 가리킨다.
"""


# class Sample:
#     # 멤버변수 초기화를반드시 생성자를 만들어야 한다
#     def __init__(self):  # 생성자 함수
#         self.name = '홍길동'  # 멤버 변수를 초기화 하는것!
#         self.age = 25
#         # addr = '서울' # self 없이 사용하면 호출이 되지 않음
#         print('생성자 호출')
#
#     def __del__(self):
#         print('소멸자 호출')

# 클래스 생성 = 인스턴스(객체)
# a = Sample()
# # 생성자 함수 실행 == 메모리에 올라감
# print(a.name) # 이름 출력 : 홍길동
# print(a.age) # 나이 출력 : 25

# print(addr)

# del a

# print(a) 사라져버렷



"""
    2) 
    인스턴스 함수 :  'self'인 인스턴스를 인자로 받고 인스턴스 변수와 같이 하나의 인스턴스에만 한정된 데이터를 생성, 변경, 참조
    클래스   함수 :  'cls'인 클래스를 인자로 받고 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조
    static  함수 :  클래스명 접근을 하며 객체끼리의 공유하고자 하는 메소드
    
    - 클래스 함수와 스태틱 함수는 둘 다 클래스명 접근
    - 클래스 함수는 cls를 이용하여 객체를 이용할 수 있다

"""
# class Staff:
#     def __init__(self,name):
#         self.name= name
#
#     # 일반함수 (인스턴스 함수)
#     def output(self):
#         print('{0}님은 우리 직원입니다.'.format(self.name))
#
#     @staticmethod
#     def step(name):
#         print('우리회사는 사원 직원 노비 로 구성되어 있습니다.')
#         print(name +'님은 노비 입니다')
#
#     @classmethod
#     def step2(cls,name):
#         print('우리회사는 사원 직원 노비 로 구성되어 있습니다.')
#         print(name + '님은 노비 입니다')
#         return cls(name)
#
# s2 = Staff('오민석')
# s2.output()
#
# s2.step('오민석')
# s2.output()
#
# Staff.step('홍홍이')
# s2.output()
#
# s2.step2('홍말자')
# s2.output()
#
# Staff.step2('홍딩동')
# s2.output()
#
#
# class Staff:
#     cnt = 0
#     def __init__(self,name):
#         self.name
#
#     # 일반 함수 (인스턴스 함수)
#     def output(self):
#         print('{0}님은 우리 직원입니다'.format(self.name))
#
#     @classmethod
#     def output3(cls):
#         cls.cnt += 1
#         print('총인원 :',cls.cnt)
#
# Staff.output3()



'''
     3) 클래스 상속
        - 파이션은 method overring은 있지만 method overloading 개념은 없다
        - 파이션은 다중상속이 가능
        - 부모 클래스가 2개 이상인 경우 먼저 기술한 부모클래스에서 먼저 우선 해당 멤버를 찾음
'''
class Animal :
    def move(self):
        print('동물은 움직인다')
class Wolf(Animal): # Wolf가 Animal 상속 받는다
    def move(self): # overriding
        print('늑대는 4발로 달린다')

class Human(Animal): # Human은 Animal 상속 받는다
    def move(self):
        print('인간은 2발로 걷는다')

class WolfHuman(Wolf,Human): # 앞에 기술한 것 만 print
    def move(self): #overriding
        super().move()
        print('늑대인간은 2발로 빠르게 달린다')

w = WolfHuman() # 메모리에 객체화
w.move()

