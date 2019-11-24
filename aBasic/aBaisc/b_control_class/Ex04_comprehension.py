"""
    @ 컴프리핸션 (comprehension)
    ` 하나 이상의 이터레이터로부터 파이썬 자료구조를 만드는 컴팩트한 방법
    ` 비교적 간단한 구문으로 반복문과 조건 테스트를 결합

    * 리스트 컨프리핸션
        [ 표현식 for 항목 in 순회가능객체 ]
        [ 표현식 for 항목 in 순회가능객체 if 조건 ]

    * 딕셔러리 컨프리핸션
        { 키_표현식: 값_표현식 for 표현식 in 순회가능객체 }

    * 셋 컨프리핸션
        { 표현식 for 표현식 in 순회가능객체 }

"""


# 컨프리핸션 사용하지 않은 리스트 생성
# alist = []
# alist.append(1)
# alist.append(2)
# alist.append(3)
# alist.append(4)
# alist.append(5)
# alist.append(6)
# print(alist)
#
# alist = []
# for n in range(1,6):
#     alist.append(n)
# print(alist)
#
# alist = list(range(1,6))
# print(alist)


#------------------------------------------------
# 리스트 컨프리핸션
# [예] [1,2,3,4,5,6]

# blist = [n**2 for n in range(1,7)]
# print(blist)
#
# clist = [n for n in range(1,11) if n%2 ==0]
# print(clist)
#
# rows = range(1,4)
# cols = range(1,6,2)
# dlist = [(r, c) for r in rows for c in cols]
# print(dlist)

# dlist 에서 각 요소 추출하여 출력
# for r2, c2 in dlist:
#     print(r2,c2)

#-------------------------------------------
# 딕셔러니 컨프리핸션
# {키 : 값}
# a = {x : x**2 for x in (2,3,4) } # x=2,3,4
# print(a)
#
# word = 'LOVL LOL'
# wcnt = {letter: word.count(letter) for letter in word}
# print(wcnt)
# 결과: {'L': 4, 'O': 2, 'V': 1, ' ': 1}
#------------------------------------------------
# 셋 컨프리핸션
# { 1, 2, 3, 4, 5, 6}

data = [1,2,3,1,3,5,6,2]

# alist = {n for n  in range(1,7)} # 리스트

#data input

# alist = {n for n in data}
# print(alist)
#
# # aset = {n for n in range(1,7)} # 셋
#
# aset = {n for n in data}
# print(aset)

# 리스트 컨프리핸션 과 셋 컨프리핸션의 차이는???
'''
    리스트 : 인덱스 / 중복허용 / 변경가능
    튜플 : 인덱스 / 중복허용 / 변경불가
    셋 : 인덱스 x / 중복 x / 변경가능
    딕셔너리 : 키와 밸류 / 키는 중복 x / 인덱스 x 
    

'''

# -------------------------------------------------
# [참고] 제너레이터 컨프리핸션
# ( ) 를 사용하면 튜플이라 생각하지만 튜플은 컨프리핸션이 없다.
data = [1,2,3,1,3,5,6,2]
alist = (n for n in data if n%2==1)
print(alist)
print(type(alist))
print(list(alist))

print(list(alist))
print('-'*40)

# 결과 : [1, 3, 1, 3, 5]
#       []

# 제너레이터 컨프리핸션은 한 번만 실행 한다.
# - 즉석에서 그 값을 생성해서 이터레이터를 통해 한번해 하나 씩 처리하고 저장하지 않음

