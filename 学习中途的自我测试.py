import urllib.request
url = 'http://www.jinyongshuwu.com/tian/644.html'
heads = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64'}
r = urllib.request.Request(url = url,headers = heads)
response = urllib.request.urlopen(r)
print()