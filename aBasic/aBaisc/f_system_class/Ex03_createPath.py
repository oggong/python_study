from pathlib import Path

# ------------------------------------------------
# 1. 경로의 상태보기
# print(Path.cwd())
# print(Path.home()) # 윈도우 C:/Users/계정명 리눅스 (hadoop) : /home/hadoop
#
# p = Path('Ex03_createPath.py')
# print(p.stat()) # 리눅스 스타일

# ----------------------------------------------------
# 2. 경로(파일) 생성시간 알아보기
# import stat
# import datetime
# p = Path('Ex03_createPath.py')
# print(p.stat()[stat.ST_CTIME])
# print(datetime.datetime.fromtimestamp(p.stat()[stat.ST_CTIME]))

# ------------------------------------------------
# 3. 디렉토리 생성
# p2 = Path('D:/imsi2')
# p2.mkdir(exist_ok=True)
#
# p3 = Path('imsi2/myclass/python')
# p3.mkdir(parents=True) # 도움말 보고 찾으세욤


# ------------------------------------------------
# 4. 파일 생성 -> open(w모드)
# imsi / a.txt 파일에 '홍길동 화이팅' 쓰기
# p4 = open('imsi/a.txt','w',encoding='utf-8')
# data ="홍길동 화이팅"
# p4.write(data)
# p4.close()
#
# p = Path('imsi/a.txt')
# with open(p,'wt',encoding='utf-8') as f:
#     f.write('홍길동 파이팅')
#
# p =Path('imsi/z.txt')
# p.touch()

# a.txt 파일명을 test.txt 파일명으로 변경

# p5 = Path('imsi/a.txt')
# p5.rename('imsi/test.txt')

# rename은 여러개 바꿀수 있다 replace 파일 덮어쓰기
# p6 = Path('imsi/test.txt')
# p6.replace('imsi/test1.txt')

# ------------------------------------------------
#  5. 경로 제거
# f = Path('imsi/z.txt')
# # f.rmdir()
# f.unlink()
import os
f2 = Path('imsi/a.txt')
os.remove('imsi/a.txt')