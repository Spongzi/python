import re
import requests
from bs4 import BeautifulSoup
findwz = re.compile(r'<div class="content">(.*)</div>')
#找到自己想要爬的网站，然后定义一个值，并且给其赋值
url = 'https://ishuo.cn/'
#对网页发送访问请求
visit_url = requests.get(url)
# print(visit_url.status_code)  #查看页面访问码
# 对得到的网页源码进行解码操作
visit_url.encoding = 'utf-8'
r = visit_url.text
#在源码中找到自己想要爬取的内容
find1 = BeautifulSoup(r,'lxml')
wz1 = find1.find_all('div',class_="content")
for itme in wz1:
    itme = str(itme)
    wz = re.findall(findwz,itme)[0]
    if wz.find("li") == -1:
        print(wz)