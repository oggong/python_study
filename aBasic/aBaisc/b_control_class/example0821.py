# 1. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
# list_1 = [0, 3, 1, 7, 5, 0, 5, 8, 0, 4]
#
# def quiz_2(list_data):
#     a = set(list_data)
#     return (list(a)[1:5])
# quiz_2(list_1)

# ➀{1, 3, 4, 5} ➁[1, 3, 4, 5] ➂{3, 1, 7, 5} ➃{0, 3, 1, 7} ➄[3, 1, 7, 5]

# 답 2

# # 2. 각 자료구조에 대한 설명이다. (가) ~ (라)에 알맞은 용어를 쓰시오.
# (가) 나중에 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조로, LIFO(Last In First Out)로 구현된다.
############ 스택
# (나) 먼저 넣은 데이터를 먼저 반환하도록 설계된 메모리 구조로, FIFO(First In First Out)로 구현된다.
############ 큐
# (다) 값의 변경이 불가능하며, 리스트의 연산, 인덱싱, 슬라이싱 등을 동일하게 사용한다.
############ 시퀀스
# (라) 값을 순서 없이 저장하면서 중복을 불허한다.
############ 셋

# 3. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?


# def delete_a_list_element(list_data, element_value):
#     if element_value in list_data:
#         list_data.remove(element_value)
#         return list_data
#     else:
#         return "False"
# list_data = ['a', 1, 'gachon', '2016.0']
# element = float(2016)
# result = delete_a_list_element(list_data, element)
# print(result)

# ➀ Error ➁['a', 1, 'gachon'] ➂ None ➃ False ➄['a', 1, 'gachon', '2016.0']

# 답 4


# 4. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?


a = [3, "apple", 2016, 4]
b = a.pop(0)
c = a.pop(1)
print(b + c)

# ➀ 2019 ➁ Error ➂ 2010 ➃ 6 ➄ apple

# 답 1

# 5. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)
def quiz_1(data_1, data_2):
    result = []
    for i in (tuple_1 + tuple_2):
        result.append(i)
    return (result)
print(quiz_1(tuple_1, tuple_2))

# ➀ [1, 2, 3, 4, 5, 6] ➁[(1, 2, 3) (4, 5, 6)] ➂ (1, 2, 3) (4, 5, 6) ➃ [(1, 2, 3, 4, 5, 6)] ➄(1, 2, 3, 4, 5, 6)

# 답 1

# 6. 다음 코드의 실행 결과를 쓰시오.

dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
    dict_2[dict_values[i]] = dict_keys[i]
print(dict_2[2])

# 답 4

# 7. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

animal = ['cat', 'snake', 'monkey', 'ant', 'spider']
legs= [4, 0, 2, 4, 8]
animal_legs_dict = {}
for i in range(len(animal)):
    animal_legs_dict[legs[i]] = animal[i]
    animal_legs_dict['ant'] = 6
print(animal_legs_dict)

# ➀ {0: 'snake', 8: 'spider', 2: 'monkey', 6: 'ant', 4:'cat'}
# ➁ {0: 'snake', 8: 'spider', 2: 'monkey', 4: 'ant', 4:'cat', 'ant': 6}
# ➂ {0: 'snake', 8: 'spider', 2: 'monkey', 4: 'ant','ant': 6}
# ➃ {4: 'ant', 0: 'snake', 2: 'monkey', 8: 'spider','ant': 6}
# ➄ {0: 'snake', 8: 'spider', 2: 'monkey', 6: 'ant'}

# 답 3

# 8. 다음 코드의 실행 결과를 쓰시오.

Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)

# 답 10

# 9. 다음 코드의 실행 결과를 쓰시오.

a = list(range(10))
print(a)
a.append(a[3])
print(a)
a.pop(a[3])
print(a)
a.insert(3, a[-1])
print(a)
a.pop()
print(a)

# 답 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 10. 다음 코드의 실행 결과를 쓰시오.


data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}
for k in ['one','two','three']:
    try:
        print(data_1[k][:1])
    except TypeError:
        print("error")
for k in ['one', 'two','three']:
    try:
        data_1[k][-1] = "a"
        print(data_1[k][-1])
    except TypeError :
        print("error")

# (1,)
# [1]
# error
# error
# a
# a