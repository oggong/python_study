'''

    exfile3.py
        mypackage / example/ exmodule.py 안에 sum() 함수 호출

'''

#1
from example.exmodule import sum
print(sum(3,7))

#2
import example.exmodule
# sum = example.exmodule.sum(3,7)
# print(sum)
print(example.exmodule.sum(3,7))

#3
from example import exmodule
print(exmodule.sum(3,7))