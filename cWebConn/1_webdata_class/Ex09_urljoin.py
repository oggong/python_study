"""
 urllib.parse.urljoin() : 상대경로를 절대경로로 변화하는 함수
"""

from urllib import parse

baseUrl = 'httpL//www.example.com/html/a.html'

print(parse.urljoin(baseUrl, 'b.html'))
print(parse.urljoin(baseUrl, '/c.html'))
print(parse.urljoin(baseUrl, '../sub/d.html'))
print(parse.urljoin(baseUrl, 'sub/e.html'))
print(parse.urljoin(baseUrl, '/sub/f.html'))

print(parse.urljoin(baseUrl,'http://www.mysite.com/mypage.jsp'))