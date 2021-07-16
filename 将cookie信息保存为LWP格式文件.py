import urllib.request
import urllib.parse
import http.cookiejar
import json

# 登陆请求地址
url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
# 将表单数据转换成bytes类型，并设置编码utf-8
data = bytes(urllib.parse.urlencode({'username': 'lxl921sx615', 'password': 'lxl921sx615'}), encoding='utf-8')
cookie_file = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(cookie_file)
# 生成cookie处理器
cookie_processor = urllib.request.HTTPCookieProcessor(cookie)
# 创建opener对象
opener = urllib.request.build_opener(cookie_processor)
# 发送登陆请求
response = opener.open(url, data=data)
response = json.loads(response.read().decode('utf-8'))['msg']
print(response)
if response == '登录成功！':
    # 保存cookie文件
    cookie.save(ignore_discard = True,ignore_expires=True)
else:
    print("傻逼")
