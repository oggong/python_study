"""
 간단하게 크롬 브라우저를 실행하여 페이지 열기
"""
from selenium import webdriver

# 1. webdriver 객체생성
# driver = webdriver.Chrome('D:/mywork/Python/cWebConn/4_selenium_class/webdriver/chromedriver.exe')
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
# 2. 페이지 접근
driver.get('http://www.google.com')
# 3. 화면을 캡처해서 저장하기
driver.save_screenshot('WebSite.png')


bt = driver.find_element_by_name('q')
bt.send_keys("플레이데이터")
bt.submit()