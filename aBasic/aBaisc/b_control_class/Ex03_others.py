str = 'HELLO'                # 문자열
li = ['a','b','c']        # 리스트
tpl = ('ㄱ','ㄴ','ㄷ')    # 튜플
di = dict(k=5, j=6)       # 딕셔너리

# (1) unpacking
a ,b ,c = tpl
print(b) # ㄴ

alist = [(1,2),(3,4),(5,6)]
for(first,second) in alist:
    print(first+second)
# s 3 7 11

# (2) zip()
days = ['월','화','수']
doit = ['잠자기','공부','놀기','먹기']

time = [10,12,2,4,6]

for yoil, halil in zip(days,doit):
    print(yoil,halil)
print(list(days,doit,time))
