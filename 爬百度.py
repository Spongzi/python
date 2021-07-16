import urllib.request
import urllib.parse

url = 'http://www.jinyongshuwu.com/tian/644.html'

response = urllib.request.urlopen(url = url)

print(response.read().decode('utf-8'))