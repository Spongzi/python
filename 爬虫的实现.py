from lxml import etree
import time
import random
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

#处理空白符
def processing(strs):
    s=''
    for n in strs:
        n=''.join(n.split())#去除空字符
        s = s+n#拼接字符串
def get_move_info(url):
    response = requests.get(url , headers = headers)
    html = etree.HTML(response.text)
    div_all = html.xpath('//div[@class="info"]')
    for div in div_all:
        names = div.xpath('./div[@class="hd"]/a//span/text()')
        name = processing(names)
        infos = div.xpath('./div[@class="bd"]/p/text()')
        info = processing(infos)
        score = div.xpath('./div[@class="bd"]/div/span[2]/text()')
        print("电影名：",name)
        print("导演与演员：",info)
        print("评分：",score)
        print("---分割线---")
if __name__ == "__main__":
    for i in range(0,250,25):
        url = 'https://movie.douban.com/top250?start={page}&filter='.format(page = i)
        get_move_info(url)
        time.sleep(random.randint(1,3))
