from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req



# 1. webdriver 객체생성
driver = webdriver.Chrome('D:/mywork/Python/cWebConn/4_selenium_class/webdriver/chromedriver.exe')

# 2. 페이지 접근
url = "https://comm.news.nate.com/Comment/ArticleComment/List?artc_sq=20190419n35031&order=&cmtr_fl=0&prebest=0&clean_idx=&user_nm=&fold=&mid=n0400&domain=&argList=0&best=1&return_sq=&connectAuth=N&page={}#comment"

review_list = []

for i in range(1, 14):
    link = url.format(i)
    driver.get(link)
    driver.implicitly_wait(2)

    html = driver.page_source
    soup.BeautifulSoup()