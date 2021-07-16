import urllib.request
import urllib.parse

url = 'https://httpbin.org/post'

#将表单数据转换成bytes类型，并设置编码方式为uft-8
data = bytes(urllib.parse.urlencode({'hellp':'python'}),encoding='utf-8')

response = urllib.request.urlopen(url=url,data=data)#发送网络请求

print(response.read().decode('utf-8'))