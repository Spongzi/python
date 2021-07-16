import urllib.request
import http.cookiejar
#登陆后页面的请求地址
url = 'http://site2.rjkflm.com:666/index/index/index.html'
cookie_file = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar()
#读取cookie文件内容
cookie.load(cookie_file,ignore_expires=True,ignore_discard=True)
#生成cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
#创建opener对象
opener = urllib.request.build_opener(handler)
response = opener.open(url)
print(response.read().decode('utf-8'))