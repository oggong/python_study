# 1. 패키지(packages)에 대한 설명 중 틀린것은?
#
# ① 다양한 모듈의 합으로 디렉터리로 연결된다.
# ② 하나의 대형 프로젝트를 만드는 코드의 묶음이다.
# ③ 개별 .py 파일을 의미한다.
# ④ 다양한 오픈소스들이 관리되는 방법이다.
# ⑤ _ _init_ _, _ _main_ _ 등키워드 파일명이 사용된다.

# 답 3

# 2. ‘game’이라는 패키지를 만들고 싶다고 가정하자.
# 패키지를만들기 위해 디렉터리별로 필요한 모듈을 구현하고자 한다. 다음 그림에서 빈칸에 들어가야 할 파일은?

# ➀ __main__ ➁import game ➂ __init__.py ➃ __main__.py ➄__init__

# 답 3

# 3. 두 코드 파일인 ‘fah_converter.py’와‘module_ex.py’는 같은 디렉터리에 있다.
# 다음과같은 결과값을 얻기 위해 빈칸에 들어갈 적합한 코드를 쓰시오.

# fah_converter.py

# import fah_converter as fah
#
# def covert_c_to_f(celsius_value):
#     return celsius_value * 9.0 / 5 + 32
# test_value = 0

# module_ex.py


# print ("Enter a celsius value: ")
# celsius = float(input())
# fahrenheit = fah.covert_c_to_f(celsius)
# print ("That's ", fahrenheit, " degrees Fahrenheit")

# 실행 결과
# Enter a celsius value:
# 100
# That's 212.0 degrees Fahrenheit

# 4. 모듈을 호출하는 방법이 아닌 것은?

# ➀ import os ➁ import os as * ➂ from os import listdir ➃ from os import * ➄ import os as linuxos

# 답 2

# 5. ‘calculator_input.py’는 사칙연산 프로그램이다. 다음 빈칸을 채워 프로그램을 완성하시오.
# calculator.py

# def sum_func(a, b):
#     return a + b
# def multiply_func(a,b):
#     return a * b
# def minus_func(a,b):
#     return a -b
# def devide_func(a,b):
#     return a / b

#calculate_input.py

# from calculator import *
# user_input = input("사칙연산 프로그램: ").split(" ")
#
# first_val , second_val = int(user_input [0]), int(user_input [2])
#
# fourcal = user_input[1]
#
# if fourcal == "+":
#     result = sum_func(first_val , second_val)
# elif fourcal == "-":
#     result = minus_func(first_val , second_val)
# elif fourcal == "/":
#     result =devide_func(first_val , second_val)
# else:
#     result =multiply_func(first_val , second_val)
# print("실행 결과는", result)