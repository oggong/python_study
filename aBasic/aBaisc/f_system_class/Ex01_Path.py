"""
 - import pathlib 만 선언하면
        Path클래스 사용시 pathlib.Path라고 명시해야 한다. 
"""
from pathlib import Path
# p = Path('C:\Windows2')
# p = Path('.') # 상대경로
p = Path('..') # 상대경로의 부모까지 찾아온다
print(p)
print(p.resolve()) #  상대경로 찾아온다

result = []
for x in p.iterdir():
    if x.is_dir():
        result.append(x)
print(result)  # 하위 목록들 출력

# 위와 동일하게 comprehension 방식

result2 = [x for x in p.iterdir() if x.is_dir()]
print(result2)

# glob() 이용
sub = list(p.glob('**/*.py')) # 자손 디렉터리 중에서 data 디렉터리안에 csv 파일만 찾기
print(sub)

# (1) 해당 경로와 하위 목록들 확인


# (2) 파일시스템에 해당 파일이 존재하는지 여부


# (3) 윈도우는 경로 구분자로 역슬래쉬를 사용하지만 Path를 사용하면 슬래쉬로도 인식하여
# 운영체제의 영향없이 추상화하여 path를 사용할 수 있다

