import re
import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
get_url = requests.get(url,headers=headers)
print(get_url.status_code)
get_url.encoding = 'utf-8'
url_text = get_url.text
r = BeautifulSoup(url_text,'lxml')
r_find = r.find_all('div',class_="hd")
re_name = re.compile(r'<span class="title">(.*)</span>')
for item in r_find:
    item = str(item)
    name = re.findall(re_name,item)[0]
    print(name)