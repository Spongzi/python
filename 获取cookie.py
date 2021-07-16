import urllib.request
import urllib.parse
import http.cookiejar
import json

# 登陆请求地址
url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'
# 将表单数据转换成bytes类型，并设置编码utf-8
data = bytes(urllib.parse.urlencode({'username': 'lxl921sx615', 'password': 'lxl921sx615'}), encoding='utf-8')
# 创建cookie对象
cookie = http.cookiejar.CookieJar()
# 生成cookie处理器
cookie_processor = urllib.request.HTTPCookieProcessor(cookie)
# 创建opener对象
opener = urllib.request.build_opener(cookie_processor)
# 发送登陆请求
response = opener.open(url, data=data)
response = json.loads(response.read().decode('utf-8'))['msg']
print(response)
if response == '登录成功！':
    # 循环遍历cookie的内容
    for i in cookie:
        # 打印成功登陆的cookie信息
        print(i.name + '=' + i.value)
else:
    print("获取失败")
