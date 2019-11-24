"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1: 'one', 2: 'two', '3': 'three', 1: 'again'}

print(dt)

print(dt[1])
# do it 저자에 의하면 1번 중 어떠한 것이 나올거라는 보장이 없음

print(dt['3'])

print('#' * 50)

# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스는 안된다
dt2 = {1: 'one', 2: 'two', (3, 4): 'tuple'}

# tuple 추출
print(dt2[(3, 4)])

print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
dt2['korea'] = 'seoul'
print(dt2)

dt2['korea'] = 'incheon'
print(dt2)

print('--------- 3. Key로 Value값 찾기  --------------- ')

print(dt2['korea'])

# 여러개 추가할 때 (update() 이용)

dt2['korea'] = 'seoul', 'incheon'
print(dt2)

dt2.update(Gyeongggi='Guri', Gyeongsang='Busan')
print(dt2)


# print(dt2[3]) #존재하지 않는 3 키 값으로 추출
#     ---------->error

print('#'*50)
# 존재 하지 않지만 에러 발생하지 않게 하려면 get
print(dt2.get(3))
print(dt2.get(3,'Pocheon'))
print('#'*50)

# Key와 Value만 따로 검색
print(dt2.keys())
print(dt2.values())

print(dt2.items())

# 단, 딕셔너리는 순서가 정해져 있지 않다
