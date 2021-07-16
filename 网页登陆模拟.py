import urllib.request
import urllib.parse

url = 'http://site2.rjkflm.com:666/index/index/chklogin.html'

#将表单数据转换成bytes类型，并设置编码utf-8
data = bytes(urllib.parse.urlencode({'username':'lxl921sx615','password':'lxl921sx615'}),encoding = 'utf-8')

#创建一个request对象
r = urllib.request.Request(url=url,data = data,method='POST')

response = urllib.request.urlopen(r)

print(response.read().decode('utf-8'))