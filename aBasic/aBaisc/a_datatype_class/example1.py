# a = int(input('정수를 입력하세요 >>'))
# b = int(input('정수를 입력하세요 >>'))
# c = int(input('정수를 입력하세요 >>'))
# d = int(input('정수를 입력하세요 >>'))
# e = int(input('정수를 입력하세요 >>'))
#
# # avg = (a+b+c+d+e)/5
#
# num_list = [a,b,c,d,e]
#
# avg = sum(num_list, 0.0) / len(num_list)
#
# print("평균 >>",avg)
#
# count = 0
# for i in range(0,len(num_list)):
#     if num_list[i] > avg:
#      count+=1
#
# print("평균을 상회하는 숫자의 갯수 >>",count)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# a = [10,20,30,40,50]
# a.reverse()
# print(a)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 정수를 입력

# a = int(input('정수를 입력하세요 >>'))
# b = int(input('정수를 입력하세요 >>'))
# c = int(input('정수를 입력하세요 >>'))
# d = int(input('정수를 입력하세요 >>'))
# e = int(input('정수를 입력하세요 >>'))
#
# num_list = [a,b,c,d,e]
#
# avg = sum(num_list, 0.0) / len(num_list)
#
# print("평균 >>",avg)
#
#
# import numpy
# print(numpy.std(num_list))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# 4
strnum = {1:'', 2: 'ABC', 3: 'DEF', 4: 'GHI',5:'JKL',6:'MNO',7:"PQRS",8:"TUV",9:"WXYZ"}

strinput = input('문자열을 입력하세요 >>')

for i in strinput:
    for j in strnum.keys():
        if strnum[j].__contains__(i):
            print(j,end=" ")







