import re

# https://wikidocs.net/4308
# findall(검색어, 문자열) : 문자열에서 검색어와 일하는 내용들을 리스트로 반환

msg = 'We_are_happy!! You are happy?? Happy2019-2020 안녕'

# result = re.match('.*happy', msg)
# if result:
#     print(result.group())
# print('-' * 20)

# serach()
# result = re.search('happy', msg)
# if result:
#     print(result.group())

# split()
# result = re.split('a', msg)
# print(result)

# sub()
# result = re.sub('a', '@', msg)
# print(result)
# print('*' * 20)

# findall()
# a = re.findall('happy', msg)
# print(a)
# print('-'*30)

# 소문자 찾기
# a = re.findall('[a-z]',msg)
# print(a)
# print('-'*30)

## 소문자가 아닌것들 찾기
# a = re.findall('[^a-z]',msg)
# print(a)
# print('-'*30)

## 소문자(반복) 모두 찾기
# a = re.findall('[a-z]+',msg)
# print(a)
# print('-'*30)

## 소문자와 대문자 찾기
# a = re.findall('[a-zA-Z]',msg)
# print(a)
# print('-'*30)

## 숫자 찾기
# a = re.findall('[0-9]',msg)
# print(a)
# print('-'*30)

# 소문자/대문자/숫자 아닌 거 찾기
a = re.findall('[^a-zA-Z0-9]',msg)
print(a)
print('-'*30)

# 영문자 숫자 _ 를 검색 // \w == 특수 문자가 빠짐 \W == 특수문자만 나옴

a = re.findall('[\W]+', msg)
print(a)
print('-'*30)


