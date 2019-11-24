"""
경로 이동은  Path 모듈로 안되어 os 모듈이 필요하다
"""
from pathlib import Path
import os

# print(Path.cwd())
# os.chdir('..')
# print(Path.cwd()) // 디렉토리 체인지

# 리눅스에서 주로 사용

# print(os.environ["HOMEPATH"]) # 윈도우 경우
# sub = Path("hadoop/myproject/myjob")
# p = Path(os.environ["HOMEPATH"],sub)
# print(p)

# ===================================
import shutil

# shutil.rmtree('imsi2') # 내부에 파일이 있어도 지워짐

# shutil.copy('Ex00.txt',Path('copy.txt')) # 디렉터리는 만들어주지 않음

shutil.copytree('.','../f_copy') # 현재 디렉터리를 한번에 복사

