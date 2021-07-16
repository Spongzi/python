import urllib.request
import urllib.error
import socket

url = 'https://www.python.org/'
try:
    #发送网络请求，设置超时时间为0.1秒
    response = urllib.request.urlopen(url = url,timeout=1)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as error:
    if isinstance(error.reason , socket.timeout):
        print("当前任务已经超时，即将执行下一个任务")