"""
    collections 모듈: 파이썬의 내장 모듈
    (1) deque : 스택과 큐를 모두 지원하는 모듈
    (2) OrderedDict : 순서를 가진 딕셔러니 객체
    (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
                  같은 이름의 키의 값을 하나로 만들 때 사용
    (4) Counter : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
    (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
"""

# -------------------------------------
# (1) deque : 스택과 큐를 모두 지원하는 모듈
#           - 리스트와 비슷한 형식으로 데이타를 저장한다.
#           - append() 함수로 기존 리스트처럼 데이터가 인덱스 번호와 저장된다

# import collections -> collections.deque.xxxx

# from collections import deque  # deque.xxxxx
#
# deque_list = deque()
# for i in range(5):  # 0,1,2,3,4
#     deque_list.append(i)
# deque_list.pop()  # 스택 처럼
# deque_list.pop()
#
# deque_list.insert(1, 99)
# print(deque_list)  # 결과 : 0 , 99 , 1 , 2

# -------------------------------------------
# (2) OrderedDict 모듈 : 순서를 가진 딕셔러니 객체
#                기본적인 딕셔너리는 순서를 보장하지 않는 객체이다

# d = {}  # 빈 딕셔너리 생성
# d['z'] = 100
# d['b'] = 200
# d['s'] = 300
# d['a'] = 400
# # for i in d :
# #     print(i) # key 만 나옴
#
# for k, v in d.items():
#     print(k, v)  # 순서 대로 나옴 !!!! 지금은 순서대로 나오나 보장이 안되욤

# from collections import OrderedDict
#
# d = OrderedDict()  # 순서 딕셔너리 생성
# d['z'] = 100
# d['b'] = 200
# d['s'] = 300
# d['a'] = 400
# for k, v in d.items():
#     print(k, v)

# ----------------------------------------------
# (3) defaultdict : 딕셔너리 변수를 생성할 때 키에 대한 기본 값을 지정
#                   같은 이름의 키의 값을 하나로 만들 때 사용

# d=dict() # 빈 딕셔너리 생성
# print(d['first'])
# [에러발생] - 생성하지 않은 키를 호출

# from collections import defaultdict
#
# d = defaultdict(lambda: 0)  # lambda 뒤에 인자가 들어와야 하나 지금은 빈칸 처리 = 어떤 인자가 들어와도 0값 반환
# print(d['first'])  # 0
# print(d.items())  # dict_items([('first', 0)])
#
# s = [('yellow', 1), ('blue', 2), ('red', 5), ('yellow', 3), ('blue', 2)]
# d = defaultdict(list)  # 초기값 형태를 list 구조로
# for k, v in s:
#     d[k].append(v)
# print(d.items()) # dict_items([('yellow', [1, 3]), ('blue', [2, 2]), ('red', [5])])
# ---------------------------------------------------
# (4) Counter 모듈 : 시퀀스 자료형의 데이터 값의 개수를 딕셔너리 형태로 반환하는 자료구조
# from collections import Counter
# text = list('gooooooood')
# c = Counter(text)
# print(c)

# 딕셔너리 형식의 초깃값이 들어올 때
# # c = Counter({'yellow':5, 'red':2})
# print(c)
# print(list(c.elements()))


# -------------------------------------------------
# (5) namedtuple : 튜플의 형태로 데이터 구조체를 저장하는 방법
from collections import namedtuple

MyPoint = namedtuple('MyPoint',['x','y'])
p = MyPoint(100,200)
print(p.x,p.y)
print(p.x + p.y)