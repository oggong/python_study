# 1. 다음 코드의 실행 결과를 쓰시오.

# def test(t):
#     t = 20
#     print("InFunction:", t)
# x = 10
# print("Before:", x)
# test(x)
# print("After:", x)

# 답 : Before: 10
#      InFunction: 20
#      After: 10

# 2. 다음 코드의 실행 결과를 쓰시오.
# def sotring_function(list_value):
#     return list_value.sort()
# print(sotring_function([5,4,3,2,1]))

# 답 None

# 3. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

# def is_yes(your_answer):
#     if your_answer.upper() == "YES" or your_answer.upper() == "Y":
#         result = your_answer.lower()
# print(  is_yes("Yes"))

# ➀ Error ➁'Yes' ➂ None ➃ 'yes' ➄ 'YES'

# 답 3 None

# 4. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

# def add_and_mul(a, b, c):
#     return b + a * c + b
# print(add_and_mul(3, 4, 5) == 63)
# ➀ 63 ➁ 2.39 ➂ True ➃ False ➄5.23

# 답 4

# 5. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?
# def args_test_3(one, two, *args, three):
#
#     print(one + two + sum(args))
#     print(args)
# args_test_3(3, 4, 5, 6, 7)
# ➀ 25 (5, 6, 7) ➁ 20(6, 7) ➂ TypeError ➃ 25(6, 7) ➄ 20 (5, 6, 7)
# 답 3

# 6. 다음 코드의 실행 결과를 쓰시오.

# def rain(colors):
#     colors.append("purple")
#     colors = ["green", "blue"]
#     return colors
# rainbow = ["red", "orange"]
# print(rain(rainbow))

# 답: ['green', 'blue']

# 7. 다음 코드의 실행 결과를 쓰시오.

# def function(value):
#     print(value ** 3)
# print(function(2))

# 8
# None

# 8. 다음 코드의 실행 결과를 쓰시오.
# def get_apple(fruit):
#     fruit = list(fruit)
#     fruit.append("e")
#     fruit = ["apple"]
#     return fruit
# fruit = "appl"
# get_apple(fruit)
# print(fruit)

# 답 : apple

# 9. 다음과 같이 코드를 작성했을 때, 실행 결과로 알맞은 것은?

# def return_sentence(sentence, n):
#     sentence += str(n)
#     n -= 1
#     if n < 0:
#         return sentence
#     else:
#         return(return_sentence(sentence, n))
# sentence = "I Love You"
# print(return_sentence(sentence, 5))

# ➀ None ➁ I Love You ➂ I Love You543210
# ➃ I Love You54321 ➄ ILove You5

# 답 3

# 10. 다음 코드의 실행 결과를 쓰시오.

# def test(x, y):
#     tmp = x
#     x = y
#     y = tmp
#     return y.append(x)
# x = ["y"]
# y = ["x"]
# test(x, y)
# print(y)

# 답 ['x']

# 11. 다음 코드를 실행하면 결과값으로 120이 나온다. 빈칸에 들어갈 알맞은 코드를 작성하시오.
def factorial_calculator(n):
    if n in (0, 1):
        return 1
    else:
        return n * factorial_calculator(n-1)
print(factorial_calculator(5))

# 답 :   return n * factorial_calculator(n-1)


