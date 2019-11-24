# 1. 다음 코드의 실행 결과를 쓰시오

# a = [0, 1, 2, 3, 4]
# print(a[:3], a[:-3])

# 답 [0, 1, 2] [0, 1]

# 2. 다음 코드의 실행 결과를 쓰시오.

# a = [0, 1, 2, 3, 4]
# print(a[::-1])

# 답 [4, 3, 2, 1, 0]

# 3. 다음 코드의 실행 결과를 쓰시오.

# first = ["egg", "salad", "bread", "soup", "canafe"]
# second = ["fish", "lamb", "pork", "beef", "chicken"]
# third = ["apple", "banana", "orange", "grape", "mango"]
# order = [first, second, third]
# john = [order[0][:-2], second[1::3], third[0]]
# del john[2]
# john.extend([order[2][0:1]])
# print(john)

# 답 :[["egg","salad","brad"],["lamb","pork"],["apple"]]

# 4. 다음 코드의 실행 결과를 쓰시오.

# list_a = [3, 2, 1, 4]
# list_b = list_a.sort()
# print(list_a, list_b)

# 답 [3, 2, 1, 4] None

# 5. 다음 코드의 실행 결과를 쓰시오.

# fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
# print(fruits[-3:], fruits[1::3])

# 답 ['orange', 'strawberry', 'melon'] ['banana', 'orange']

# 6. 다음 코드의 실행 결과를 쓰시오.

# num = [1, 2, 3, 4]
# print(num * 2)

# 답 : [1, 2, 3, 4, 1, 2, 3, 4]

# 7. 다음 코드의 실행 결과를 쓰시오.

# a = [1, 2, 3, 5]
# b = ['a', 'b', 'c','d','e']
# a.append('g')
# b.append(6)
# print('g' in b, len(b))

# 답 : False 6

# 8. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

# list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
# list_b=[ ]
# for i in range(len(list_a)):
#     if i % 2 != 1:
#         list_b.append(list_a[i])
#         print(list_b)

# 답 ['Hankook']
#    ['Hankook', 'is']
#    ['Hankook', 'is', 'academic']
#    ['Hankook', 'is', 'academic', 'located']
#    ['Hankook', 'is', 'academic', 'located', 'South Korea'] # 3번

# 9. 다음 코드를 실행한 후, 2018과 "2018"을 각각 입력했을 경우 알맞은 실행 결과끼리 묶인 것은?

# admission_year = input("입학 연도를 입력하세요: ")
# print(type(admission_year))

# 답 : ➂ <class ‘str’>, <class ‘str’>

# 10. 다음 코드의 실행 결과를 쓰시오.
# from builtins import print
#
# country = ["Korea", "Japan", "China"]
# capital = ["Seoul", "Tokyo", "Beijing"]
# index = [1, 2, 3]
# country.append(capital)
# country[3][1] = index[1:]
# print(country)

# 답: ['Korea', 'Japan', 'China', ['Seoul', [2, 3], 'Beijing']]

# 11. 다음과 같이 코드를 작성했을 때 예측되는 실행 결과를 쓰고, 이러한결과가 나오는 이유에 대해 서술하시오.
# ( is키워드는 주소를 비교한다 )

# a = [5, 4, 3, 2, 1]
# b = a
# c = [5, 4, 3, 2, 1]
# a is b
# print(id(a is b))
# # 답 : True 주소값이 값음 140736138160464
# a is c
# # 답 : False 주소값이 다름 140736138160496
# print(id(a is c))

# 12. 다음 코드를 실행하면 다음과 같은 결과가 나온다. 그이유에 대해 서술하시오.
# (is 키워드는 주소를 비교한다 )

# a = 1
# b = 1
#
# print(id(a))
# print(id(b))
# a is b
# print(id(a is b))
# print(a is b)
# # True a 140736138682768 = b 140736138682768
# a = 300
# b = 300

# print(id(a))
# print(id(b))

# a is b
# print(id(a is b))
# print(a is b)
# # False

# 15. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

list_1 = [[1, 2], [3], [4, 5, 6]]
a,b,c = list_1
list_2 = a + b + c
print(list_2)