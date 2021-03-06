from requests_html import HTMLSession,UserAgent

#创建HTML会话对象
session = HTMLSession()
#创建一个随机请求头
ua = UserAgent().random
#发送网络请求
r = session.get('https://news.youth.cn/jsxw/index.htm',headers = {'user-agent': ua})
#编码
r.encoding = 'gb2312'
if r.status_code == 200:
    li_all = r.html.xpath('.//ul[@class="tj3_1"]/li')
    for li in li_all:
        news_title = li.find('a')[0].text
        news_href = "https://news.youth.cn/jsxw"+\
                    li.find('a[href]')[0].attrs.get('href').lstrip('.')
        news_time = li.find('font')[0].text
print(news_time)
print(news_title)
print(news_href)