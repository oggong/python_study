# import urllib.request
from urllib import request

url = 'http://www.google.com'
site = request.urlopen(url)
# print(site)
page = site.read()
print(page)
print('-'*50)

print(site.status)
print('-'*50)
headers = site.getheaders()
print(headers)
print('-'*50)
#헤더 정보의 이름과 값으로 출력
for name,value in headers:
    print('-' * 50)
    print("name :",name,end=' ')
    print("value : ",value)
    print('-' * 50)