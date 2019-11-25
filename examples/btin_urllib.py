# -*- coding: utf-8 -*-

from urllib import request
import json

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

# 解析json为python对象
def fetch_data(url):
    req = request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0')
    with request.urlopen(req) as f:
        return json.loads(f.read().decode('utf-8'))

# 测试
URL = 'http://m.maoyan.com/ajax/movieOnInfoList?token='
data = fetch_data(URL)
print(data)
assert data['stid']== '576591972453269000'
print('ok')
