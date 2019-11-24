from bs4 import BeautifulSoup
from urllib import request as req
from urllib import parse

import MySQLdb  # MySQLdb 설정

# db 연결
conn = MySQLdb.connect(host='localhost', user='scott', passwd='tiger', db='pythondb')

conn.set_character_set('utf-8')

cur = conn.cursor()

# 1. 데이타 가져오기

base_url = 'https://web.dominos.co.kr/goods/'
for k in ['C0102', 'C0201', 'C0202', 'C0203']:
    print("==" * 50)
    html = req.urlopen('https://web.dominos.co.kr/goods/list?dsp_ctgr={0}'.format(k))

    soup = BeautifulSoup(html, 'html.parser')
    # print(soup)

    img = soup.select('.prd_img_view img')
    if k == 'C0102':
        price_L = soup.select('.price_large')
        price_M = soup.select('.price_medium')
    else:
        price = soup.select('.price_num')

    # print(btn_Url)
    if k in ['C0102', 'C0201']:
        btn_Url = soup.select('.btn_detail')

    for j, i in enumerate(img):
        title = i.attrs['alt']
        img = i.attrs['src']

        if k == 'C0102':
            price_l = price_L[j].text
            price_m = price_M[j].text
            print(title, img, price_l, price_m)
        else:
            price_side = price[j].text
            print(title, img, price_side)

        if k in ['C0102', 'C0201']:
            btn_url = btn_Url[j].attrs['href']
            detail_url = parse.urljoin(base_url, btn_url)
            res_det = req.urlopen(detail_url)
            soup1 = BeautifulSoup(res_det, 'html.parser')
            detail = soup1.select_one('.detail_view_info').text
            print(detail.strip())

        print("*" * 50)
