
# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = "http://fanyi.baidu.com/"
    req = requests.get(url = target)
    req.encoding = 'utf-8'   #转译成utf-8的形式
    print(req.text)