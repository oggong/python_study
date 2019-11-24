'''Ex03_json.py'''

import json

# f = open('./data/temp.json','rt',encoding='utf-8')
# json_data = f.read()
# data = json.loads(json_data)
# print(data)
# # for item in data:
# #     print('>',item)
# f.close()

#  (1) 이름 : xxxxxx
#      번호 : x
#      직업 : xxxx

#  (2) with 구문에 예외 처리로 수정해주세요

try :
    with open('./data/temp.json','rt',encoding='utf-8') as f:
        json_data = f.read()
        data = json.loads(json_data)
        for item in data:
            print('이름 :', item)
            for detail in data[item]:
                if detail == "No":
                    print('번호 :',data[item][detail])
                if detail == "Job":
                    print('직업 :',data[item][detail])

except FileNotFoundError as e:
    print(e)
else:
    f.close()
