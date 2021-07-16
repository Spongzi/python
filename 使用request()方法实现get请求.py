import urllib3
#关闭ssl警告
urllib3.disable_warnings()
jindong_url = 'https://www.jd.com/'
python_url = 'https://www.python.org/'
baidu_url = 'https://www.baidu.com/'
#创建连接池管理对象
http = urllib3.PoolManager()
r1 = http.request('GET',jindong_url)
r2 = http.request('GET',python_url)
r3 = http.request('GET',baidu_url)
print(r1.status)
print(r2.status)
print(r3.status)