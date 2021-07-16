import urllib.request

url = 'https://www.python.org/'#请求地址

#发送网络请求，设置超时时间
response = urllib.request.urlopen(url = url,timeout=0.5)

print(response.read().decode('utf-8'))