import requests

#发送网络请求
response = requests.get('https://www.jd.com/')
response.encoding = 'utf-8'

print(response.text)