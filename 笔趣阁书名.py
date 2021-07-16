import re
import requests
from bs4 import BeautifulSoup

def get_name(wz1):
    get_wz1 = requests.get(wz1)
    get_wz1.encoding = 'utf-8'
    wz1_text = get_wz1.text
    r1 = BeautifulSoup(wz1_text, 'lxml')
    r1_find = r1.find_all('div',id="info")
    get_name_find = re.compile(r'<h1>(.*)</h1>')
    for item1 in r1_find:
        item1 = str(item1)
        name1 = re.findall(get_name_find,item1)
        # print(name1)
        return name1
url = 'https://www.biqugeu.net/'
get_url = requests.get(url)
print(get_url.status_code)
wz = re.compile(r'<a href="(.*)"')
get_url.encoding = 'utf-8'
url_text = get_url.text
r = BeautifulSoup(url_text,'lxml')
r_find = r.find_all('div',class_="item")
data = []
for item in r_find:
    item = str(item)
    name = re.findall(wz,item)[0]
    sever = 'https://www.biqugeu.net'
    wz1 = sever+name
    s_name = get_name(wz1)
    print(s_name)
    print(wz1)
